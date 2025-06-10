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
  def create_fernet_key_from_password(password):
    """
    Creates a 32 url-safe base64-encoded bytes Fernet key from given string input.

    Args:
      password (str): The key to be encoded.

    Returns:
      Fernet: Fernet object with acceptable key.
    """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_32bit_password = hashed_password[:32] # bcrypt makes a 60-bit hash, we only need 32-bits.
    fernet_key = base64.urlsafe_b64encode(hashed_32bit_password)

    return fernet.Fernet(fernet_key)

  @staticmethod
  def encrypt(plaintext, password):
    """
    Encrypt the given plaintext using a given key via symmetric encryption.

    Args:
      plaintext (str): The plaintext to be encrypted.
      password (str): String user password to be used as the key.

    Returns:
      bytes: The encrypted plaintext.
    """
    plaintext_bytes = plaintext.encode('utf-8')

    fernet_key = Encryption.create_fernet_key_from_password(password)
    ciphertext = fernet_key.encrypt(plaintext_bytes)

    return ciphertext

  @staticmethod
  def decrypt(ciphertext, password):
    """
    Decrypt the given ciphertext using a given key via symmetric encryption.

    Args:
      ciphertext (bytes): The ciphertext to be decrypted.
      password (str): String user password to be used as the key.

    Returns:
      bytes: The decrypted ciphertext, junk if incorrect key or ciphertext.
    """
    fernet_key = Encryption.create_fernet_key_from_password(password)
    plaintext = fernet_key.decrypt(ciphertext)

    return plaintext