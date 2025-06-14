import base64
import bcrypt
import cryptography.fernet as fernet

class Hashing:
  """Interface class to handle the hashing requirements."""

  @staticmethod
  def hash(input):
    """
    Create a hash of the input using bcrypt.

    Args:
      input (str): The input to be hashed.

    Returns:
      bytes: The hashed input.
    """

    # bcrypt stores the salt alongside the hashed value
    input_bytes = input.encode('utf-8')
    input_hash = bcrypt.hashpw(input_bytes, bcrypt.gensalt())

    return input_hash

  @staticmethod
  def verify_hash(input, hash):
    """
    Confirm the hash of the input matches the given hash.

    Args:
      input (str): The challenge input.

    Returns:
      bool: Whether the input challenge hash matches the given hash.
    """
    input_bytes = input.encode('utf-8')
    return bcrypt.checkpw(input_bytes, hash)

class Encryption:
  """Interface class to handle the symmetric encryption requirements."""