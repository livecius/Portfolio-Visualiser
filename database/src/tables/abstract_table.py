class AbstractTable:
  def __init__(self, connection):
    self.connection = connection
    self.cursor = self.connection.cursor()

    self.initialise_table()

  def initialise_table(self):
    """
    Initialise a table if it doesn't already exist.
    """
    raise NotImplementedError

  def insert(self):
    """
    Insert a row into the database.
    """
    raise NotImplementedError