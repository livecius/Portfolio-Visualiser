class AbstractTable:
  def __init__(self, connection):
    self.connection = connection
    self.cursor = self.connection.cursor()

    self.initialise_table()

  def initialise_table(self):
    raise NotImplementedError