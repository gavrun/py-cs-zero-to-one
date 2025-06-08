# 07_python_advanced/standard_library_secrets.py

# Python 'secrets' module
# For cryptographically secure random numbers and tokens

import secrets
import string

# Random integer in range [0, n)
print("randbelow(10):", secrets.randbelow(10))  # e.g., 7

# Random bit generator (returns integer)
print("randbits(8):", secrets.randbits(8))      # e.g., 203 (0..255)

# Random choice from sequence (secure)
choices = ['red', 'green', 'blue']
print("choice:", secrets.choice(choices))       # e.g., 'blue'

# Generate secure random tokens

# Hex token (length = n bytes → 2n hex chars)
token1 = secrets.token_hex(16)     # 32-char hex string
print("token_hex:", token1)

# URL-safe base64 token (length = n bytes)
token2 = secrets.token_urlsafe(16)  # shorter, URL-friendly
print("token_urlsafe:", token2)

# Raw bytes
token3 = secrets.token_bytes(16)
print("token_bytes:", token3)

# Generate secure password
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for _ in range(12))
print("secure password:", password)


# secrets.randbelow(n)        → secure random int in [0, n)
# secrets.randbits(k)         → int with k random bits
# secrets.choice(seq)         → secure random element
# secrets.token_bytes(n)      → n random bytes
# secrets.token_hex(n)        → hex-encoded token (2n chars)
# secrets.token_urlsafe(n)    → base64-encoded URL-safe token

# For all security-sensitive randomness: use secrets, not random.

