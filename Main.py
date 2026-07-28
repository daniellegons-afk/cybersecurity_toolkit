from port_scan import run_scanner
from password_generator import run_password_genrator
from ceaser_ciph import run_cipher
from login_sys import run_login_system

def main_menu():
    while True:
        print("\n================================")
        print("     CYBERSECURITY TOOLKIT")
        print("================================")
        print("1. Port Scanner")
        print("2. Password Generator")
        print("3. Caesar Cipher")
        print("4. Login System")
        print("5. Exit")
        print("================================")

        choice = input("Please pick one: ")

        if choice == "1":
            run_scanner()
        elif choice == "2":
            run_password_genrator()
        elif choice == "3":
            run_cipher()
        elif choice == "4":
            run_login_system()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again")

main_menu()
