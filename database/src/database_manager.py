import os
from security import cryptography_services
import sqlite3
from tables import user, broker, api_keys, portfolio

class DatabaseManager:
  """
  Facade class to encapsulate database logic.
  """
  DATA_PATH = os.path.join(os.path.dirname(__file__), "../data")
  DATABASE_FILE_PATH = os.path.join(DATA_PATH, "database.db")

  def __init__(self, database_path = None):
    if database_path is None:
      database_path = self.DATABASE_FILE_PATH

      if not os.path.exists(self.DATA_PATH):
        os.makedirs(self.DATA_PATH)

    self.connection = sqlite3.connect(database_path)

    self.User = user.User(self.connection)
    self.Broker = broker.Broker(self.connection)
    self.ApiKeys = api_keys.ApiKeys(self.connection)
    self.Portfolio = portfolio.Portfolio(self.connection)

  def add_user(self, email, password):
    """
    Add a user to the database, hashing their passwords.

    Args:
      email (str): The user's email
      password (str): The user's password

    Yields:
      sqlite3.IntegrityError: User with email already exists.
    """
    password_hash = cryptography_services.Hashing.hash(password)
    self.User.insert(email, password_hash)