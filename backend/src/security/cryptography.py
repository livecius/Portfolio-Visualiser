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
  def create_fernet_key(key):
    return fernet.Fernet(key)

  @staticmethod
  def encrypt(plaintext, key):
    """
    Encrypt the given plaintext using a given key via symmetric encryption.

    Args:
        plaintext (str): The plaintext to be encrypted.
        key (str): The symmetric encryption key.

    Returns:
        bytes: The encrypted plaintext.
    """
    key_bytes = key.encode('utf-8')
    plaintext_bytes = plaintext.encode('utf-8')

    fernet_key = Encryption.create_fernet_key(key_bytes)
    ciphertext = fernet_key.encrypt(plaintext_bytes)

    return ciphertext

  @staticmethod
  def decrypt(ciphertext, key):
    """
    Decrypt the given ciphertext using a given key via symmetric encryption.

    Args:
        ciphertext (bytes): The ciphertext to be decrypted.
        key (str): The symmetric encryption key.
    """
    key_bytes = key.encode('utf-8')

    fernet_key = Encryption.create_fernet_key(key_bytes)
    plaintext = fernet_key.decrypt(ciphertext)

    return plaintext