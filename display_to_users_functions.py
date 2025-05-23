import csv

from Terminal_colors import Colors
from is_float import is_float
from Custom_Errors import CsvError

def display_balance(user_id):
    """
    Displays:
        - the balance of a specific user from the banking system's CSV file.

    Raises:
        CsvError:
            - If the 'user_balance' in the CSV is not a valid float or integer,
              or has an invalid format (e.g., too many decimal points).
            - If the provided user_id is not found in the CSV file.
    """
    color = Colors()
    BLUE, GREEN, UNDERLINE, RESET = color.blue, color.green, color.underline, color.reset
    file_name = "gab's_banking_system_users.csv"
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        user_exists = False
        
        for row in reader:
            if row["user_ids"] == user_id:
                current_balance = row["user_balance"]
                
                if is_float(current_balance) and ('.' in current_balance):
                    balance_list = current_balance.split(".")
                    peso, centavo = balance_list

                    if peso.isdigit() and centavo.isdigit():
                        print(f"\n{BLUE}{row["usernames"]}'s balance: {RESET}")
                        print(f"{GREEN}{UNDERLINE}P{float(current_balance):,.2f}{RESET}")
                        user_exists = True
                        break
                    elif len(balance_list) > 3:
                        raise CsvError("Error in displaying balance: invalid centavo values") 
                    else:
                        raise CsvError("Error in displaying balance: invalid peso and centavo values")
                    
                elif row["user_balance"].isdigit():
                    print(f"\n{BLUE}{row["usernames"]}'s balance: {RESET}")
                    print(f"{GREEN}{UNDERLINE}P{float(current_balance):,.2f}{RESET}")
                    user_exists = True
                    break

        if not user_exists:
            raise CsvError("Error in displaying balance: invalid centavo values")



def display_user_information(user_id):
    """
    Displays: 
        - the full name of a specific user.
        - ID number of a specific user.

    Raises:
        CsvError: If an unexpected error occurs during file processing.
    """
    color = Colors()
    BLUE, RESET, BBLUE, UNDERLINE = color.blue, color.reset, color.bblue, color.underline
    file_name = "gab's_banking_system_users.csv"
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        
        try:
            for row in reader:
                if row["user_ids"] == user_id:
                    full_name = row["usernames"]
                    print(f"\n{BLUE}Full name: {BBLUE}{UNDERLINE}{' '.join(word.capitalize() for word in row['usernames'].split())}{RESET}")
                    print(f"{BLUE}Id number: {BBLUE}{UNDERLINE}{user_id}{RESET}")
        except Exception as e:
            raise CsvError(e)
        
        
def display_user_navigation(user_id):
    """
    Displays: 
        - A personalized welcome message  
        - The menu of navigation options for a user.

    Raises:
        CsvError:
            - If the provided user_id is not found in the CSV file.
            - If a FileNotFoundError occurs when trying to open the CSV file.
    """
    color = Colors()
    RED, YELLOW, BLUE, RESET = color.red, color.yellow, color.blue, color.reset
    file_name = "gab's_banking_system_users.csv"
    try:
        id_not_found = True
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    print(f"\n{YELLOW}Hello {' '.join(word.capitalize() for word in line['usernames'].split())}!{RESET}")
                    print(f"{BLUE}Enter any number to navigate for your account.{RESET}")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Display balance")
                    print("4. Display User Information")
                    print("5. Log-out")
                    id_not_found = False
            
            
            if id_not_found:
                raise CsvError(f"{RED}Something went wrong the to user id.{RESET}")     
            
    except FileNotFoundError as e:
        print("{RED}File Error in display_user_navigation:{RESET}")
        raise CsvError(e)