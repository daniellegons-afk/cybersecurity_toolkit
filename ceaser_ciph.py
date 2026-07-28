def run_cipher():

    message = input("What is your message? ")

    while True:
        try:
            key = int(input("What is the key? "))
            break
        except ValueError:
            print("invalid input please enter a number ")

    while True:
        choice = input("Encrypt or decrypt? ").lower()
        if choice == "encrypt" or choice == "decrypt":
            break
        else:
            print("Invald, try again")

    result = ""  

    for char in message:
        if choice == "encrypt":
            if char.isalpha():
                shifted = ord(char) + key
                if char.islower() and shifted > ord('z'):
                    shifted -= 26  # wrap back around
                elif char.isupper() and shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
            else:
                result += char
        elif choice == "decrypt":
            if char.isalpha():
                shifted = ord(char) - key
                if char.islower() and shifted < ord('a'):
                    shifted += 26
                elif char.isupper() and shifted < ord('A'):
                    shifted += 26
                result += chr(shifted)
            else:
                result += char

    print(f"Result: {result}")
        