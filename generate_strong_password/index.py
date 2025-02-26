import secrets
import string
import random

def generate_strong_password(length=20):
    if length < 12 or length > 50:
        raise ValueError("Password length must be between 12 and 50 characters")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    # Ensure at least one of each required type
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    # Fill the rest of the password with random choices
    all_chars = lowercase + uppercase + digits + symbols
    password_chars += [secrets.choice(all_chars) for _ in range(length - 4)]

    # Shuffle to randomize order
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

# Generate a strong password with a random length between 12 and 50
password_length = random.randint(12, 50)
print(generate_strong_password(password_length))
