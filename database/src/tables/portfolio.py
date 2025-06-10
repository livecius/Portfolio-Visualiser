from tables.abstract_table import AbstractTable

class Portfolio(AbstractTable):
  """
  Facade manager for the Portfolio Table.

  You should not instantiate this class directly, use the exposed methods through DatabaseManager.
  """
  def initialise_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS portfolio (
      portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER,
      api_key_id INT,
      portfolio_data JSON NOT NULL,
      FOREIGN KEY (user_id) REFERENCES user(user_id),
      FOREIGN KEY (api_key_id) REFERENCES broker(api_key_id)
    );
    """)