import hashlib

def run_login_system():
    
    def register():
        user_name = input("Please enter your username: ")
        password = input("Please enter your password:")

        hash = hashlib.sha256(password.encode()).hexdigest()

        with open("credentials.txt", "w") as file:
            file.write(f"{user_name}\n")
            file.write(f"{hash}\n")
        
        with open("credentials.txt", "r") as file:
            content = file.read()
            content.strip()
            print(f"{content}")    

        print("Registration successful")
    

    def login():
        attempts = 0 
    
        while attempts < 3:
            attempted_user_name = input("please enter your username:")
            attempted_password = input ("please enter your password:")
    
            attempted_hash = hashlib.sha256(attempted_password.encode()).hexdigest()
        
            with open ("credentials.txt", "r") as file:
                stored_username = file.readline().strip()
                stored_hash = file.readline().strip()
        
            if attempted_user_name == stored_username and attempted_hash == stored_hash:
                print("Access Granted!")
                break
            else:
                attempts += 1
                remaining = 3 - attempts
                if remaining > 0:
                    print(f"Access Denied! {remaining} attempts remaining")
                else:
                    print("Account locked!")
            
            
    def main():
        while True:
            choice = input("Would you like to register or login?: ").lower()
            if choice == "register":
                register()
                break
            elif choice == "login":
                login()
                break
            else:
                print("Invalid choice")


    main()






