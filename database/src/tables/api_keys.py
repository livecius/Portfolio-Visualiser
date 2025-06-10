from tables.abstract_table import AbstractTable

class ApiKeys(AbstractTable):
  """
  Facade manager for the ApiKeys Table.

  You should not instantiate this class directly, use the exposed methods through DatabaseManager.
  """
  def initialise_table(self):
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_keys (
      api_keys_id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INT,
      broker_id INT,
      api_key TEXT,
      secret_key TEXT,
      FOREIGN KEY (user_id) REFERENCES user(user_id),
      FOREIGN KEY (broker_id) REFERENCES broker(broker_id),
      CONSTRAINT fk_user_broker UNIQUE (user_id, broker_id) -- api_key must exist for a user / broker relation
    );
    """)