# Testing libraries for generating passwords

# Takes as per mistral - using standard lib for gnerating passwords

import secrets
import string

def generate_password(length=22):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print(generate_password())
