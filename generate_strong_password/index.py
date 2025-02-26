import secrets
import string

def generate_strong_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print(generate_strong_password())
