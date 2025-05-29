import os

from Essentials.Terminal_colors import Colors
from Essentials.Custom_Errors import CsvError

from csv_file_checker_functions.check_database_content import check_database_content
from csv_file_checker_functions.check_database_file import check_database_file
from authentication_handlers.handle_authentication import handle_authentication
from handle_user_choice_prompt import handle_user_choice_prompt



def main():
    color = Colors()
    GREEN, RED, BLUE, BOLD, RESET = color.green, color.red, color.blue, color.bold, color.reset
    
    main_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = "gabs_banking_system_users.csv"
    full_file_path = os.path.join(main_directory, file_name)

    print(f"{check_database_file(full_file_path)}")
    
    while True:
        try:
            check_database_file(full_file_path)
            check_database_content(full_file_path)
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
            
            authenticated_id = handle_authentication(user_authentication_option, full_file_path) # returns a string

            # goes back to user authentication if the string value is false(empty) -- (when continue is triggered by the else statement)
            if authenticated_id:
                handle_user_choice_prompt(authenticated_id, full_file_path)
            else:
                continue


        except ValueError as e:
            print(f"{BOLD}{RED}\nError:{RESET}{RED}{e}{RESET}")
            print(f"{RED}Please enter a valid input and try again\n{RESET}")
            
        except FileNotFoundError as e:
            print(f"{BOLD}{RED}File not found error:{RESET} {RED}{e}{RESET}")
            return
        
        except IOError as e:
            print(f"{BOLD}{RED}Error in Input/Output:{RESET} {RED}{e}{RESET}")
            
        except CsvError as e:
            print(f"{BOLD}{RED}Error in the csv file: {RESET}{RED} {e} {RESET}")
            print(f"{RED}Please undo any changes to the banking system database file.\n{RESET}")
            
        except Exception as e:
            print(f"{BOLD}{RED}Unexpected error: {RESET}{RED} {e} {RESET}")
        
        
if __name__ == "__main__":
    main()

        