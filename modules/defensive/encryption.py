from cryptography.fernet import Fernet
import os

def generate_key(save_path="key.key"):
    """
    Generates an encryption key and saves it to a file.
    """
    key = Fernet.generate_key()
    with open(save_path, "wb") as f:
        f.write(key)
    return key

def load_key(key_path="key.key"):
    """
    Loads an encryption key from a file.
    """
    return open(key_path, "rb").read()

def encrypt_file(file_path, key):
    """
    Encrypts a file and overwrites it.
    """
    f_obj = Fernet(key)
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    encrypted_data = f_obj.encrypt(file_data)
    
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

def decrypt_file(file_path, key):
    """
    Decrypts a file and overwrites it.
    """
    f_obj = Fernet(key)
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    
    decrypted_data = f_obj.decrypt(encrypted_data)
    
    with open(file_path, "wb") as f:
        f.write(decrypted_data)

if __name__ == "__main__":
    # Example usage (uncomment to test locally)
    # key = generate_key()
    # encrypt_file("test.txt", key)
    # decrypt_file("test.txt", key)
    pass
