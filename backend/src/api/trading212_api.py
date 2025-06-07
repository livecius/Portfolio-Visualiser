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

  # Account Data
  def fetch_account_data(self):
    return self.requests("GET", "/api/v0/equity/account/cash")

  def fetch_account_metadata(self):
    return self.requests("GET", "/api/v0/equity/account/info")

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
      response = requests.get(url, headers=headers)
    else:
      raise KeyError(f"Unknown HTTP method: {method}")

    response.raise_for_status()
    return response.json()