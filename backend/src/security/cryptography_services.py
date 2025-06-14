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

  @staticmethod
  def get_fernet_key_from_password(password, salt = None):
    """
    Generate a valid key from a password.

    Args:
      password (str): The password to be converted.
      salt (bytes): Optional salt for fernet key creation. Default is created by bcrypt

    Returns:
      fernet_key (bytes): The generated key.
      salt (bytes): The salt used for fernet key creation.
    """
    if salt is None:
      salt = bcrypt.gensalt()

    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # Use [7:39] as the first 6 indexes are reserved for
    # algorithm identifier and number of rounds separated by $ symbols
    fernet_key = base64.urlsafe_b64encode(hashed_password[7:39])

    return fernet_key, salt

  @staticmethod
  def encrypt(plaintext, password, salt = None):
    """
    Encrypt the given plaintext using fernet symmetric encryption.

    Args:
      password (str): The password key.
      plaintext (str): The plaintext to be encrypted.
      salt (bytes): Optional salt for fernet key creation. Default is created by bcrypt

    Returns:
      ciphertext (bytes): The ciphertext.
      salt (bytes): The salt used for fernet key creation.
    """
    fernet_key, salt = Encryption.get_fernet_key_from_password(password, salt)
    fernet_object = fernet.Fernet(fernet_key)

    plaintext_bytes = plaintext.encode('utf-8')
    ciphertext_bytes = fernet_object.encrypt(plaintext_bytes)

    return ciphertext_bytes, salt

  @staticmethod
  def decrypt(ciphertext, password, salt):
    """
    Decrypt the given ciphertext using fernet symmetric encryption.

    Args:
      ciphertext (bytes): The ciphertext to be decrypted.
      password (str): The password key.
      salt (bytes): The salt used for fernet key creation.

    Returns:
      string: Decrypted decoded ciphertext.
    """
    fernet_key, _ = Encryption.get_fernet_key_from_password(password, salt)
    fernet_object = fernet.Fernet(fernet_key)

    return fernet_object.decrypt(ciphertext).decode('utf-8')