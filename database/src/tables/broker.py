from tables.abstract_table import AbstractTable

class Broker(AbstractTable):
  """
  Facade manager for the Broker Table.

  You should not instantiate this class directly, use the exposed methods through DatabaseManager.
  """
  def initialise_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS broker (
      id INTEGER PRIMARY KEY AUTOINCREMENT
    );
    """)