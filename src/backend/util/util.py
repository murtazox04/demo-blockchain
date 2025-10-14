import hashlib


def hash_string(input_string):
    """Two rounds of SHA256"""
    return hashlib.sha256(hashlib.sha256(input_string).digest()).digest()
