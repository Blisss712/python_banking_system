import os

from Terminal_colors import Colors
from create_new_account import create_new_account
from verify_user_account import verify_user_account

# returns user_id or a false value
def handle_authentication(user_option: str):
    color = Colors()
    RED, RESET = color.red, color.reset
    current_path = os.getcwd()
    file_name = "gab's_banking_system_users.csv"
    
    if os.path.exists(current_path+"\\"+ file_name):
        if user_option == 1:
            authenticated_id = verify_user_account(file_name)
            return authenticated_id
        
        elif user_option == 2:
            forced_login = create_new_account(file_name) # always returns false 
            return forced_login
        
    else:
        raise FileNotFoundError(f"{RED}User database has been edited/deleted.{RESET}")