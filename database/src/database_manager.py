import os
import sqlite3
from tables import user

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

  def add_user(self, email, password):
    self.User.add_user(email, password)