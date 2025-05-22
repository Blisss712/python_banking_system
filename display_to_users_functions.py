import csv

from Terminal_colors import Colors
from is_float import is_float
from Custom_Errors import CsvError

def display_balance(user_id):
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
    color = Colors()
    BLUE, RESET, BOLD = color.blue, color.reset, color.bold
    file_name = "gab's_banking_system_users.csv"
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        
        try:
            for row in reader:
                if row["user_ids"] == user_id:
                    full_name = row["usernames"]
                    print(f"\n{BLUE}Full name: {BOLD}{full_name.capitalize()}{RESET}")
                    print(f"{BLUE}Id number: {BOLD}{user_id}{RESET}")
        except Exception as e:
            raise CsvError(e)
        
        
def display_user_navigation(user_id):
    color = Colors()
    RED, YELLOW, BLUE, RESET = color.red, color.yellow, color.blue, color.reset
    file_name = "gab's_banking_system_users.csv"
    try:
        id_not_found = True
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    print(f"\n{YELLOW}Hello {line['usernames'].capitalize()}!{RESET}")
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