from tables.abstract_table import AbstractTable

class ApiKeys(AbstractTable):
  """
  Facade manager for the ApiKeys Table.

  You should not instantiate this class directly, use the exposed methods through DatabaseManager.
  """
  def initialise_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_keys (
      id INTEGER PRIMARY KEY AUTOINCREMENT
    );
    """)