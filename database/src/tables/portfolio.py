from tables.abstract_table import AbstractTable

class Portfolio(AbstractTable):
  """
  Facade manager for the Portfolio Table.

  You should not instantiate this class directly, use the exposed methods through DatabaseManager.
  """
  def initialise_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS portfolio (
      id INTEGER PRIMARY KEY AUTOINCREMENT
    );
    """)