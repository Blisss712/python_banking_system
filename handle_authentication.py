"""
Args:
    It takes the prompted string user_authentication option in the main function

Returns:
    A string -> which is regarded as 'True' to proceed to log-in
    False -> which can be regarded as empty string to deny log-in access
    
"""

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
        raise FileNotFoundError(f"{RED}User may have edited or deleted the database.{RESET}")