#!/usr/bin/env python3
from cryptography.fernet import Fernet

def generate_key() -> bytes:
    return Fernet.generate_key()

def encrypt(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data)

def decrypt(token: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(token)

def main():
    key = generate_key()
    message = b'Secret message'
    cipher = encrypt(message, key)
    plain = decrypt(cipher, key)
    print(f"Encrypted: {cipher}\nDecrypted: {plain}")

if __name__ == '__main__':
    main()
