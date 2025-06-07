import datetime
from dev_config import TRADING212_API_KEY
import requests


class Trading212:
  """
  API interface to retrieve Trading212 portfolio data.

  https://t212public-api-docs.redoc.ly/
  """
  BASE_URL = "https://live.trading212.com"

  def __init__(self, api_key = None):
    if api_key is None:
      if TRADING212_API_KEY is None:
        raise ValueError("No API key provided for Trading212. Did you forget to add to the .env?")

      api_key = TRADING212_API_KEY

    self.api_key = api_key

  @staticmethod
  def build_query_params(**kwargs):
    query = {}

    for key, value in kwargs.items():
      query[key] = value

    return query

  @staticmethod
  def get_epoch_as_iso8601_utc():
    epoch = datetime.datetime.fromtimestamp(0, datetime.timezone.utc)
    return epoch.strftime("%Y-%m-%dT%H:%M:%SZ")

  # Account Data
  def fetch_account_data(self):
    return self.requests("GET", "/api/v0/equity/account/cash")

  def fetch_account_metadata(self):
    return self.requests("GET", "/api/v0/equity/account/info")

  # Personal Portfolio
  def fetch_all_open_positions(self):
    return self.requests("GET", "/api/v0/equity/portfolio")

  def search_for_a_specific_position_by_ticker(self, ticker):
    return self.requests("POST", "/api/v0/equity/portfolio/ticker", {"ticker": ticker})

  def fetch_a_specific_position(self, ticker):
    return self.requests("GET", "/api/v0/equity/portfolio/ticker", {"ticker": ticker})

  # Historical Items
  def historical_order_data(self, cursor = 0, ticker = "", limit = 50):
    query = Trading212.build_query_params(limit=limit, cursor=cursor, ticker=ticker)

    return self.requests("GET", "/api/v0/equity/history/orders", query)

  def paid_out_dividends(self, cursor = 0, ticker = "", limit = 50):
    query = Trading212.build_query_params(limit=limit, cursor=cursor, ticker=ticker)

    return self.requests("GET", "/api/v0/equity/history/orders", query)

  def exports_list(self):
    return self.requests("GET", "/api/v0/history/exports")

  def export_csv(
      self,
      include_dividends = True,
      include_interest = True,
      include_orders = True,
      include_transactions = True,
      time_from = None,
      time_to = None
  ):
    if time_to is None:
      time_to = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if time_from is None:
      time_from = Trading212.get_epoch_as_iso8601_utc()

    query = Trading212.build_query_params(
      dataIncluded = Trading212.build_query_params(
        includeDividends = include_dividends,
        includeInterest = include_interest,
        includeOrders = include_orders,
        includeTransactions = include_transactions
      ),
      timeFrom = time_from,
      timeTo = time_to
    )

    return self.requests("POST", "/api/v0/history/exports", query)

  def transaction_list(self, cursor = "", time = None, limit = 50):
    if time is None:
      time = Trading212.get_epoch_as_iso8601_utc()

    query = Trading212.build_query_params(
      cursor = cursor,
      time = time,
      limit = limit
    )

    return self.requests("GET", "/api/v0/history/transactions", query)

  def requests(self, method, path, params = None):
    """
    Send a REST API request to the url with the endpoint path.

    Args:
      method (str): HTTP method to use.
      path (str): Path to the api endpoint.
      params (dict): Optional parameters to pass to the request, default is None.

    Returns:
      dict: Response from the API endpoint.

    Raises:
      KeyError: Unknown method argument.
      HTTPError: HTTP request failed.
    """
    url = self.BASE_URL + path

    headers = {
      "Authorization": self.api_key,
      "Content-Type": "application/json"
    }

    response = {}

    if response == "GET":
      response = requests.get(url, headers=headers, params=params)

    elif response == "POST":
      response = requests.post(url, headers=headers, json=params)

    else:
      raise KeyError(f"Unknown HTTP method: {method}")

    response.raise_for_status()
    return response.json()