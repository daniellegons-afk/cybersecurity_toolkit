import string
import random





def run_password_genrator(length, quantity):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []

    for i in range(quantity):
        password = ""
        for j in range(length):
            password += random.choice(characters)
        passwords.append(password)

    return passwords

    