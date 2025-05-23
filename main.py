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
        GREEN, RED, BLUE, BOLD, RESET, FADED = color.green, color.red, color.blue, color.bold, color.reset, color.faded
        
        print(f"{check_database_file()}")
        
        while True:
            check_database_file()
            check_database_content()
            print(f"\n\n\n{GREEN}Welcome to Gab's Banking system!{RESET}")
            print(f"\n\n{BLUE}Enter the following numbers to navigate:{RESET}")
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
        print("File not found error:", e)
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
            print("true")
            display_user_information(user_id)
        elif user_choice == "5":
            return
        else:
            print(f"{RED}your input '{BOLD}{user_choice}{RESET}{RED}' is not in the navigation list, please enter a valid value{RESET}")


        
if __name__ == "__main__":
    main()
    # withdraw("1")
        