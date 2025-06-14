from cryptography.fernet import InvalidToken
import security.cryptography_services as cryptography
import pytest

@pytest.fixture
def hash_data():
  input_val1 = "helloworld"
  input_val2 = "goodbyeworld"

  output_hash1 = cryptography.Hashing.hash(input_val1)
  output_hash2 = cryptography.Hashing.hash(input_val2)

  return {
    "input_val1": input_val1,
    "input_val2": input_val2,
    "output_hash1": output_hash1,
    "output_hash2": output_hash2,
  }

@pytest.fixture
def encrypted_data():
  plaintext1 = "helloworld"
  plaintext2 = "goodbyeworld"

  password = "password123"

  ciphertext1 = cryptography.Encryption.encrypt(plaintext1, password)
  ciphertext2 = cryptography.Encryption.encrypt(plaintext2, password)

  return {
    "plaintext1": plaintext1,
    "plaintext2": plaintext2,
    "ciphertext1": ciphertext1,
    "ciphertext2": ciphertext2,
    "password": password,
  }

def test_compare_hash_data(hash_data):
  assert len(hash_data["output_hash1"]) > 0
  assert hash_data["input_val1"] != hash_data["output_hash1"]

  assert hash_data["output_hash1"] != hash_data["output_hash2"]

def test_verify_hash_data(hash_data):
  assert cryptography.Hashing.verify_hash(
    hash_data["input_val1"],
    hash_data["output_hash1"]
  )

  assert not cryptography.Hashing.verify_hash(
    hash_data["input_val1"],
    hash_data["output_hash2"]
  )

def test_compare_encrypted_data(encrypted_data):
  assert len(encrypted_data["plaintext1"]) > 0
  assert encrypted_data["plaintext1"] != encrypted_data["ciphertext1"]

  assert encrypted_data["ciphertext1"] != encrypted_data["ciphertext2"]

def test_decrypt_data(encrypted_data):
  assert encrypted_data["plaintext1"] == cryptography.Encryption.decrypt(
    encrypted_data["ciphertext1"],
    encrypted_data["password"]
  )

  assert encrypted_data["plaintext2"] != cryptography.Encryption.decrypt(
    encrypted_data["ciphertext1"],
    encrypted_data["password"]
  )

  with pytest.raises(InvalidToken):
    cryptography.Encryption.decrypt(encrypted_data["ciphertext1"], "wrong_password")
