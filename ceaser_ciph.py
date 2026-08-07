def run_cipher(message,key,choice):

    result = ""  

    for char in message:
        if choice == "encrypt":
            if char.isalpha():
                shifted = ord(char) + key
                if char.islower() and shifted > ord('z'):
                    shifted -= 26  
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

    return result
        