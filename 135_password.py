"""Password"""
import hashlib
def encode(password):
    """encode password to hashing SHA512 hex number"""
    password = password.encode('utf-8')
    encoded = hashlib.sha512(password).hexdigest()
    print(encoded.upper())
encode(input())
