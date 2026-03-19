import pyotp
import os
import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

DB_PATH = os.path.join(os.path.dirname(__file__), "secrets.enc")
# In a real app, the master password would be provided by the user
MASTER_SALT = b"\x14\x88\x8f\x8d\x8c\x8b\x8a\x89"

def _get_fernet():
    # Derive a key from a fixed "master" for demo purposes
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=MASTER_SALT, iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(b"CyberHub_Master_Key_v2"))
    return Fernet(key)

def save_secret(label, secret):
    data = load_secrets()
    data[label] = secret
    f = _get_fernet()
    encrypted_data = f.encrypt(json.dumps(data).encode())
    with open(DB_PATH, "wb") as file:
        file.write(encrypted_data)

def load_secrets():
    if not os.path.exists(DB_PATH):
        return {}
    try:
        f = _get_fernet()
        with open(DB_PATH, "rb") as file:
            decrypted_data = f.decrypt(file.read())
            return json.loads(decrypted_data.decode())
    except Exception as e:
        print(f"Error loading secrets: {e}")
        return {}

def delete_secret(label):
    data = load_secrets()
    if label in data:
        del data[label]
        save_secret("__DUMMY__", "__DUMMY__") # Trigger re-encryption
        data = load_secrets()
        if "__DUMMY__" in data: del data["__DUMMY__"]
        f = _get_fernet()
        with open(DB_PATH, "wb") as file:
            file.write(f.encrypt(json.dumps(data).encode()))

def generate_totp_secret():
    return pyotp.random_base32()

def get_current_code(secret):
    return pyotp.TOTP(secret).now()
