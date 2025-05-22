"""
Used in handle_authentication.py 


Arguments:
    file_name (str): The name of the CSV file where user account
                        information will be stored.

Returns:
    False: Always returns `False` to signal the calling process to
            initiate a login attempt.

"""

import csv

from Terminal_colors import Colors


def verify_user_account(file_name: str):
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