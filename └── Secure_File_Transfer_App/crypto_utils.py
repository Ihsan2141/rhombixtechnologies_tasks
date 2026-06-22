from cryptography.fernet import Fernet
import hashlib

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    cipher = Fernet(key)
    return cipher.encrypt(data)

def decrypt_data(data, key):
    cipher = Fernet(key)
    return cipher.decrypt(data)

def calculate_hash(data):
    return hashlib.sha256(data).hexdigest()