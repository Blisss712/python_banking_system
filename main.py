import csv

from Terminal_colors import Colors
from is_float import is_float
from deposit_to_user_balance import deposit
from withdraw_from_user_balance import withdraw
from display_to_users_functions import display_balance, display_user_information, display_user_navigation
from handle_authentication import handle_authentication
from file_checker import check_database_content, check_database_file
from Custom_Errors import CsvError


def main():
    try:
        color = Colors()
        GREEN, RED, BOLD, RESET = color.green, color.red, color.bold, color.reset
        
        print(check_database_file())
        print(f"\n\n\n{GREEN}Welcome to Gab's Banking system!{RESET}")
        
        while True:
            check_database_file()
            check_database_content()
            print(f"\n\nEnter the following numbers to navigate:")
            print("1. Login to your account")
            print("2. Sign up to your account")
            print("3. Exit Program\n")
            
            user_authentication_option = int(input("Input your chosen option here: ").strip())
            
            if user_authentication_option == 3:
                print(f"{GREEN}{BOLD}\nThank you for using Gab's banking system!\n{RESET}")
                print(f"{RED}Exitting program...{RESET}")
                break
            
            authenticated_id = handle_authentication(user_authentication_option) # returns a string
    
            # goes back to user authentication if the string value is false(empty) -- (when continue is triggered by the else statement)
            if authenticated_id:
                handle_user_choice_prompt(authenticated_id)
            else:
                continue
    
    except ValueError as e:
        print(f"{BOLD}{RED}\nError:{RESET}{RED} Please enter a valid input and try again\n {RESET}")
        
    except FileNotFoundError as e:
        print("Error:", e)
        return
    
    except CsvError as e:
        print(f"{BOLD}{RED}Error in the csv file: {RESET}{RED} {e} {RESET}")
        print(f"{RED}Please undo any changes to the banking system database file.\n{RESET}")
        
    except Exception as e:
        print(f"{BOLD}{RED}Unexpected error: {RESET}{RED} {e} {RESET}")
        

def handle_user_choice_prompt(user_id):
    color = Colors()
    RED, BOLD, RESET = color.red, color.bold, color.reset
    while True:
        display_user_navigation(user_id)
        user_choice = input("\nEnter your chosen option here: ")
        if user_choice == "1":
            withdraw(user_id)
        elif user_choice == "2":
            deposit(user_id)
        elif user_choice == "3":
            display_balance(user_id)
        elif user_choice == "4":
            display_user_information(user_id)
        elif user_choice == "5":
            return
        else:
            print(f"{RED}your input '{BOLD}{user_choice}{RESET}{RED}' is not in the navigation list, please enter a valid value{RESET}")


# returns user_id or a false value
def verify_user(file_name: str):
    color = Colors()
    RED, BOLD, GREEN, RESET = color.red, color.bold, color.green, color.reset 
    
    user_id = input("Enter your user id: ").strip()
    with open(file_name, newline="") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row["user_ids"] == user_id:
                passcode = input("Enter your password: ")
                attempts = 3
                
                while True:
                    if row["user_passcodes"] == passcode:
                        print(f"\n{GREEN}You have successfully signed in to your account!{RESET}")
                        return user_id
                    elif attempts >= 1:
                        print(f"{RED}{BOLD}Invalid password:{RESET}{RED}  you have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.{RESET}")
                        passcode = input("Enter your password: ")
                        attempts -= 1
                    else:
                        print(f"\n{BOLD}{RED}Login Failed{RESET}")
                        print(f"{RED}(Please enter the correct password.){RESET}")
                        return False
     
        print(f"\n{RED}{BOLD}Cannot find the user with user_id: {user_id}{RESET}")
        return False
    

    
        
if __name__ == "__main__":
    main()
    # withdraw("1")
        