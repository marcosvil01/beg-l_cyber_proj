import pyotp
import qrcode
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), "secrets.json")

def save_secret(label, secret):
    """
    Saves a secret to the local JSON database.
    """
    data = load_secrets()
    data[label] = secret
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def load_secrets():
    """
    Loads all saved secrets from the local JSON database.
    """
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

def delete_secret(label):
    """
    Deletes a secret from the database.
    """
    data = load_secrets()
    if label in data:
        del data[label]
        with open(DB_PATH, "w") as f:
            json.dump(data, f, indent=4)

def generate_totp_secret():
    return pyotp.random_base32()

def get_totp_uri(secret, name="User", issuer="CyberHub"):
    return pyotp.totp.TOTP(secret).provisioning_uri(name=name, issuer_name=issuer)

def verify_totp(secret, code):
    return pyotp.TOTP(secret).verify(code)

def get_current_code(secret):
    """
    Returns the current 6-digit TOTP code for a secret.
    """
    return pyotp.TOTP(secret).now()

if __name__ == "__main__":
    # Example usage (uncomment to test locally)
    # secret = generate_totp_secret()
    # uri = get_totp_uri(secret)
    # generate_qr_code(uri)
    pass
