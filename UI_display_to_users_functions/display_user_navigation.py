"""
Displays: 
    - A personalized welcome message  
    - The menu of navigation options for a user.

Raises:
    CsvError:
        - If the provided user_id is not found in the CSV file.
        - If a FileNotFoundError occurs when trying to open the CSV file.
"""
    
import csv

from Essentials.Terminal_colors import Colors
from Essentials.Custom_Errors import CsvError

def display_user_navigation(user_id, full_file_path):
    color = Colors()
    RED, YELLOW, BLUE, RESET = color.red, color.yellow, color.blue, color.reset
    
    
    try:
        id_not_found = True
        with open(full_file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    print(f"\n\n{YELLOW}Hello {' '.join(word.capitalize() for word in line['usernames'].split())}!{RESET}")
                    print(f"{BLUE}Enter any number to navigate for your account.{RESET}")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Display balance")
                    print("4. Display User Information")
                    print("5. Manage my account")
                    print("6. Log-out")
                    id_not_found = False
            
            
            if id_not_found:
                raise CsvError(f"{RED}Something went wrong the to user id.{RESET}")     
            
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    except Exception as e:
        raise Exception(e)
        