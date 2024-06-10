import random

def generate_token():
    # This is a low severity, low confidence issue
    # Standard pseudo-random generators are not suitable for security/cryptographic purposes.
    if random.random() > 0.5:
        return random.randint(100000, 999999)  # Low confidence

token = generate_token()
print("Generated token:", token)
