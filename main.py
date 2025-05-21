import csv
import os




class FileError(Exception):
    pass

class Colors:
    def __init__(self):
        self.red = "\033[31m"
        self.green = "\033[32m"
        self.reset = "\033[0m"
        self.bold = "\033[1m"

class Options:
    def __init__(self):
        self.yes = ["YES","Yes","yes", "yEs", "YeS", "yeS","y","Y"]
        self.no = ["No","nO","NO","N","n"]

def withdraw():
    pass

def display_balance():
    pass

def display_user_navigation():
    pass

def create_account(file_name):
    try:
        options = Options()
        while True:
            print("Type 'quit' to any options to cancel.\n")
            username = input("Enter your full name: ")
            user_id = input("Enter your unique user_id (digits only): ")
            
            if username == "quit" or user_id == "quit":
                return False
            
            if not user_id.strip().isdigit():
                raise ValueError("Please provide the necessary inputs for user_id")
            

            with open(file_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                for line in reader:
                    if line["usernames"] == username:
                        if line["user_ids"] == user_id:
                            print(f"User {username} with the id {user_id} already exists.")
                            confirm = input("Is this you? (yes/no): ")
                            if confirm in options.yes:
                                print("Please return to log-in and enter your account")
                                return False
                            elif confirm in options.no:
                                print("The given id already exists. Please create a different user id!")
                                continue
                    elif line["user_ids"] == user_id:
                        print("The given id already exists. Please create a different user id!")
                        continue
            break
                    
        while True: 
            passcode = input("Enter your new password: ")
            confirm_passcode = input("Confirm your password: ")
            
            if passcode =="quit" or confirm_passcode == "quit":
                return False
            elif passcode != confirm_passcode:
                print("Passwords do not match, please re-enter your password.")
                continue
            
            try:
                with open(file_name, "a", newline="") as file:
                    writer = csv.DictWriter(file)
                    writer.writerow({"user_ids":user_id, "usernames": username, "user_balance":0, "user_passcode":passcode})
                return True
            except IOError:
                print("Something went wrong when adding user to the csv")
            except FileNotFoundError:
                print("Something went wrong when adding user to the csv")    
            except Exception as e:
                print("Unexpected Error:",e)          
                            
    except ValueError as e:
        print("Error:",e)

def check_database_file_status():
    current_path = os.getcwd()
    file_name = "gab's_banking_system_users.csv"
    # print(current_path+"\\"+ file_name)
    
    if os.path.exists(current_path+"\\"+ file_name):
        return("\n(user database data successfully retrieved)")
        
    else:
        with open(file_name,"w",newline="") as file:
            fieldnames = ['user_ids','usernames','user_balance','user_passcodes']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
        return("\nNOTICE: new user banking database has been initialized")
        
        # option = int(input("user database doesn't exist, do you want to make a new one to continue? (Yes/No) "))
        # if option == "no" or option == "No":


def verify_user(file_name):
    color = Colors()
    user_id = input("Enter your user id: ")
    with open(file_name, newline="") as file:
        reader = csv.DictReader(file)
        stripped_id = user_id.strip()
        for row in reader:
            if row["user_ids"] == stripped_id:
                passcode = input("Enter your password: ")
                attempts = 3
                while True:
                    if row["user_passcodes"] == passcode:
                        print("You have successfully signed in to your account!")
                        return True
                    elif attempts >= 1:
                        print(f"Invalid password, you have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
                        passcode = input("Enter your password: ")
                        attempts -= 1
                    else:
                        print(f"\n{color.bold}{color.red}Login Failed{color.reset}")
                        return False
     
        print(f"\n{color.red}{color.bold}Cannot find the user with user_id: {user_id}{color.reset}")
        return False
    
    
def handle_authentication(option):
    current_path = os.getcwd()
    file_name = "gab's_banking_system_users.csv"
    # print(current_path+"\\"+ file_name)
    
    if os.path.exists(current_path+"\\"+ file_name):
        if option == 1:
            verify_user(file_name)
        elif option == 2:
            create_account(file_name)
    else:
        raise FileError("User database has been edited/deleted")
    
        
def main():
    
    try:
        color = Colors()
        print(check_database_file_status())
        # print(string)
        print("\n\n\nWelcome to Gab's Banking system!")
        while True:
            check_database_file_status()
            print("\n\nEnter the following numbers to navigate:")
            print("1. Login to your account")
            print("2. Sign up to your account")
            print("3. Exit Program\n")
            
            user_authentication_option = int(input("Input your chosen option here: "))  
            if user_authentication_option == 3:
                print(f"{color.green}{color.bold}\nThank you for using Gab's banking system!\n{color.reset}")
                break  
            is_success = handle_authentication(user_authentication_option)
            if is_success:
                display_user_navigation()
            else:
                continue
            
    except FileError as e:
        print("Error:", e)
        return
    except Exception as e:
        print("Unexpected error:",e)
        
if __name__ == "__main__":
    main()