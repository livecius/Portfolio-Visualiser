from tables.abstract_table import AbstractTable

class User(AbstractTable):
  """
  Facade manager for the User Table.

  You should not instantiate this class directly, use the exposed methods through DatabaseManager.
  """

  def initialise_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
      user_id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL,
      fernet_salt TEXT
    );
    """)

  def insert(self, email, password, fernet_salt = None):
    """
    Insert a row into the database.

    Args:
      email (str): The email address of the user.
      password (bytes || str): The password for the user.
      fernet_salt (str): The salt used in the fernet key creation.
    """
    insert_statement = """
    INSERT INTO user (email, password, fernet_salt) VALUES (?, ?, ?)
    """
    self.cursor.execute(insert_statement, (email, password, fernet_salt))
    self.connection.commit()