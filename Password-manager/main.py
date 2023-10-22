import os
from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self, key_path):
        self.key_path = key_path
        self.key = None
        self.password_dict = {}

    def generate_key(self):
        self.key = Fernet.generate_key()
        with open(self.key_path, 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        if os.path.exists(self.key_path):
            with open(self.key_path, 'rb') as key_file:
                self.key = key_file.read()
        else:
            raise FileNotFoundError(f"Key file not found at {self.key_path}")

    def encrypt_password(self, password):
        if self.key is not None:
            cipher_suite = Fernet(self.key)
            encrypted_password = cipher_suite.encrypt(password.encode())
            return encrypted_password
        else:
            raise ValueError("Key is not loaded. Please load or create a key.")

    def decrypt_password(self, encrypted_password):
        if self.key is not None:
            cipher_suite = Fernet(self.key)
            decrypted_password = cipher_suite.decrypt(encrypted_password)
            return decrypted_password.decode()
        else:
            raise ValueError("Key is not loaded. Please load or create a key.")

    def add_password(self, service, password):
        encrypted_password = self.encrypt_password(password)
        self.password_dict[service] = encrypted_password

    def get_password(self, service):
        encrypted_password = self.password_dict.get(service)
        if encrypted_password is not None:
            return self.decrypt_password(encrypted_password)
        else:
            raise KeyError(f"Password for service '{service}' not found.")

# Usage
key_path = "mykey.key"
pm = PasswordManager(key_path)
pm.generate_key()
pm.load_key()
pm.add_password("example_service", "example_password")

try:
    password = pm.get_password("example_service")
    print(f"Password for 'example_service': {password}")
except KeyError as e:
    print(e)
