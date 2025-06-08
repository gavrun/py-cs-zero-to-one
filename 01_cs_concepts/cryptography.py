# 01_cs_concepts/cryptography.py

# Cryptography Concepts 

# Cryptography is about protecting data.
# It answers questions like:
# - How can I keep this message secret?
# - How can I make sure no one has changed it?
# - How can I prove that I sent it?

# The three major ideas:
# 1. Encryption — transforms data so others can't read it
# 2. Hashing — makes a unique "fingerprint" of data (not reversible)
# 3. Keys — used to lock/unlock encrypted data (like passwords)

# Types of encryption:
# - Symmetric encryption: same key used to encrypt and decrypt
# - Asymmetric encryption: public key to encrypt, private key to decrypt


# Examples in Python


# Caesar cipher (shift cipher)

# A "cipher" is an algorithm for encrypting text, making it unreadable without a key
# This is a very old (and insecure) example of symmetric encryption.

def caesar_encrypt(text, shift):
    """Shift each letter forward by a fixed number of positions"""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(ciphertext, shift):
    """Decrypt by shifting backward"""
    return caesar_encrypt(ciphertext, -shift)

plain = "Hello, World!"
shift = 3
cipher = caesar_encrypt(plain, shift)
print("Caesar Encrypted:", cipher)
print("Caesar Decrypted:", caesar_decrypt(cipher, shift))


# Hashing (irreversible fingerprint)

# Hashing is not encryption.
# A "hash function" maps data to a fixed-size string (digest)
# It is one-way: you can't get the original data back from the hash
# Common uses: password storage, password verification, file integrity checking

import hashlib

message = "hello world"
hash_obj = hashlib.sha256(message.encode())  # SHA-256: secure hash algorithm
print("SHA-256 hash:", hash_obj.hexdigest()) # Any small change in input → completely different hash


# XOR Cipher (basic symmetric encryption)

# XOR is a very simple symmetric cipher
# Symmetric means both encryption and decryption use the same key
# XOR is not secure, but shows the idea of "masking" data with a key

def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

key = 129
encrypted = xor_encrypt_decrypt(plain, key)
print("XOR encrypted:", encrypted)
decrypted = xor_encrypt_decrypt(encrypted, key)
print("XOR decrypted:", decrypted)


# - Symmetric encryption with Fernet (AES)


# - Asymmetric encryption with RSA


# - Message authentication (HMAC)


# In real applications:
# - Use the `cryptography` package for secure encryption (e.g., AES)
# - Use salted hashing algorithms for passwords (e.g., bcrypt, argon2)
# - Never roll your own crypto for production systems

