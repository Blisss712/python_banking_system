from UI_display_to_users_functions.display_account_management_options import display_account_management_options
from account_management_handlers.account_handling_functions.change_username import change_username
from account_management_handlers.account_handling_functions.change_user_password import change_user_password
from account_management_handlers.account_handling_functions.delete_user_account import delete_user_account

def handle_account_management(user_id, full_file_path):
    try:
        while True:
            display_account_management_options()
            user_option = input("Enter your chosen option here: ")
            if user_option == "1":
                change_username(user_id, full_file_path)
            elif user_option == "2":
                change_user_password(user_id, full_file_path)
            elif user_option == "3":
                account_deleted = delete_user_account(user_id, full_file_path)
                if account_deleted:
                    return account_deleted
            elif user_option == "4":
                break
            else:
                print("Invalid option, please try again.")
                
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except Exception as e:
        raise Exception(e)
