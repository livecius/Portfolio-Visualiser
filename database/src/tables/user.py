from tables.abstract_table import AbstractTable

class User(AbstractTable):
  """
  Facade manager for the User Table.

  You should not instantiate this class directly, use the exposed methods through DatabaseManager.
  """

  def initialise_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL
    );
    """)

  def add_user(self, email, password):
    self.cursor.execute("""
    INSERT INTO user (email, password) VALUES (?, ?)
    """, (email, password))
    self.connection.commit()