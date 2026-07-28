import string
import random

def run_password_genrator():
    length = int(input("How long should each password be? "))
    quantity = int(input("How many passwords do you want? "))
    
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []

    for i in range(quantity):
        password = ""
        for j in range(length):
            password += random.choice(characters)
        passwords.append(password)

    with open("passwords.txt", "w") as file:
        for password in passwords:
            print(password)
            file.write(password + "\n")