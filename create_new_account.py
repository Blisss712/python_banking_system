"""
    The function is designed to always return 'False', which in the application
    forces a log-in attempt after the account creation process, ensuring the user
    can immediately access their newly created account.

    Returns:
        False: Always returns `False` to signal the calling process to
               initiate a login attempt.

    Raises:
        ValueError: If the user provides non-digit input for the user ID,
                    or invalid input for confirmation prompts (e.g., 'yes'/'no').
        CsvError: If an error occurs during the CSV file operations (e.g., writing).
        FileNotFoundError: If the specified CSV file does not exist when
                           attempting to write to it.
        Exception: For any other unexpected errors that may occur during the process.
"""


import csv
import os


from Custom_Errors import CsvError
from Terminal_colors import Colors
from is_float import is_float


# from handle_authentication.py
def create_new_account(file_path_name: str) -> False:  
    try:

        color = Colors()
        options = Options()
        RED, GREEN, BLUE , BOLD, RESET = color.red, color.green, color.blue, color.bold, color.reset
        while True:
            id_exists = False
            back_to_login = False
            print(f"\n{BLUE}Type '{RED}quit{RESET}{BLUE}' to any options to cancel.{RESET}")
            
            username = input("Enter your full name: ").strip()
            if username == "quit":
                return False
            elif not username.isalpha():
                print(f"{RED}Please do not include special characters in your name and try again.{RESET}")
                continue
            
            user_id = input("Enter your unique user_id (digits only): ").strip()
            if user_id == "quit":
                return False
            
            
            if not user_id.isdigit():
                raise ValueError("Please provide the necessary inputs for the user_id")
            

            with open(file_path_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                for line in reader:
                    if line["usernames"] == username:
                        if line["user_ids"] == user_id:
                            print(f"\n{RED}User '{username}' with the id [{user_id}] already exists.{RESET}")
                            confirm = input(f"{BLUE}Is this you? (yes/no): {RESET}")
                            if confirm in options.yes:
                                print(f"\n{BLUE}Please return to log-in and enter your account{RESET}")
                                back_to_login = True
                                break
                            elif confirm in options.no:
                                print("\n{RED}The given id already exists. Please create a different user id!{RESET}")
                                id_exists = True
                                break
                            else:
                                raise ValueError("Please provide the necessary inputs for the user's options")
                    elif line["user_ids"] == user_id:
                        print(f"\n{RED}The given id already exists. Please create a different user id!{RESET}")
                        id_exists = True
                        break

            if id_exists:
                continue
            elif back_to_login:
                return False
            else:
                break
                
                    
        while True: 
            passcode = input("Enter your new password: ")
            confirm_passcode = input("Confirm your password: ")
            
            if passcode =="quit" or confirm_passcode == "quit":
                return False
            elif passcode != confirm_passcode:
                print(f"{RED}Passwords do not match, please re-enter your password.{RESET}")
                continue
            
            try:
                with open(file_path_name, "a", newline="") as file:
                    fieldnames = ['user_ids','usernames','user_balance','user_passcodes']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow({"user_ids":user_id, "usernames": username, "user_balance":0, "user_passcodes":passcode})
                print(f"\n{GREEN}Successfully created user {username}.{RESET}")
                print(f"{BLUE}Please proceed to log-in.{RESET}")
                return False
            except IOError as e:
                print("Something went wrong when adding user to the csv")
                raise CsvError(e)
            except FileNotFoundError as e:
                print("Something went wrong when adding user to the csv") 
                raise FileNotFoundError(e)   
            except Exception as e:
                print("Unexpected Error:",e)          
                            
    except ValueError as e:
        print(f"\n{RED}{BOLD}An Error Occured: {RESET}{RED}{e}{RESET}")
    except Exception as e:
        print(f"\n{RED}{BOLD}An Unexpected Error Occured: {RESET}{RED}{e}{RESET}")


class Options:  # Handles input cases
    def __init__(self):
        self.yes = ["YES","Yes","yes", "yEs", "YeS", "yeS","y","Y"]
        self.no = ["No","nO","NO","no","N","n"]
        
if __name__ == "__main__":
    print(os.getcwd())