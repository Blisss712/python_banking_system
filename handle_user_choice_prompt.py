from Essentials.Terminal_colors import Colors
from Essentials.Custom_Errors import CsvError

from UI_display_to_users_functions.display_user_navigation import display_user_navigation
from UI_display_to_users_functions.display_user_information import display_user_information
from UI_display_to_users_functions.display_balance import display_balance

from balance_management_functions.deposit_to_user_balance import deposit
from balance_management_functions.withdraw_from_user_balance import withdraw

from account_management_handlers.handle_account_management import handle_account_management

def handle_user_choice_prompt(user_id: str, full_file_path: str) -> None:
    color = Colors()
    RED, BOLD, RESET = color.red, color.bold, color.reset
    try:
        while True:
                display_user_navigation(user_id, full_file_path)
                user_choice = input("\nEnter your chosen option here: ")
                if user_choice == "1":
                    withdraw(user_id, full_file_path)
                elif user_choice == "2":
                    deposit(user_id, full_file_path)
                elif user_choice == "3":
                    display_balance(user_id, full_file_path)
                elif user_choice == "4":
                    display_user_information(user_id, full_file_path)
                elif user_choice == "5":
                    account_deleted = handle_account_management(user_id, full_file_path)
                    if account_deleted:
                        return
                elif user_choice == "6":
                    return
                else:
                    print(f"{RED}your input '{BOLD}{user_choice}{RESET}{RED}' is not in the navigation list, please enter a valid value{RESET}")
   
    except ValueError as e:
        raise ValueError(e)        
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    
    except CsvError as e:
        raise CsvError(e)        
    except Exception as e:
        raise Exception(e)