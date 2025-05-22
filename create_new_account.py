import csv
import os


from Custom_Errors import CsvError
from Terminal_colors import Colors
from is_float import is_float


# Always returning false allows forced log-in after the signing up process.
def create_new_account(file_name: str) -> False:
    try:

        color = Colors()
        options = Options()
        RED, BOLD, RESET = color.red, color.bold, color.reset
        while True:
            id_exists = False
            back_to_login = False
            print(f"Type '{BOLD}quit{RESET}' to any options to cancel.\n")
            username = input("Enter your full name: ").strip()
            user_id = input("Enter your unique user_id (digits only): ").strip()
            
            if username == "quit" or user_id == "quit":
                return False
            
            if not user_id.isdigit():
                raise ValueError("Please provide the necessary inputs for the user_id")
            

            with open(file_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                for line in reader:
                    if line["usernames"] == username:
                        if line["user_ids"] == user_id:
                            print(f"\nUser '{username}' with the id [{user_id}] already exists.")
                            confirm = input("Is this you? (yes/no): ")
                            if confirm in options.yes:
                                print("\nPlease return to log-in and enter your account")
                                back_to_login = True
                                break
                            elif confirm in options.no:
                                print("\nThe given id already exists. Please create a different user id!")
                                id_exists = True
                                break
                            else:
                                raise ValueError("Please provide the necessary inputs for the user's options")
                    elif line["user_ids"] == user_id:
                        print("\nThe given id already exists. Please create a different user id!")
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
                print("Passwords do not match, please re-enter your password.")
                continue
            
            try:
                with open(file_name, "a", newline="") as file:
                    fieldnames = ['user_ids','usernames','user_balance','user_passcodes']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow({"user_ids":user_id, "usernames": username, "user_balance":0, "user_passcodes":passcode})
                print(f"Successfully created user {username}")
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
        print(f"\n{RED}An Error Occured: {e}{RESET}")
    except Exception as e:
        print(f"\n{RED}An Unexpected Error Occured: {e}{RESET}")


class Options:  # Handles input cases
    def __init__(self):
        self.yes = ["YES","Yes","yes", "yEs", "YeS", "yeS","y","Y"]
        self.no = ["No","nO","NO","no","N","n"]
        
if __name__ == "__main__":
    print(os.getcwd())