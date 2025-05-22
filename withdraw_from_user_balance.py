import csv

from Custom_Errors import CsvError
from Terminal_colors import Colors
from is_float import is_float


def withdraw(user_id):
    file_name = "gab's_banking_system_users.csv"
    
    while True:
        color = Colors()
        RED, BLUE, GREEN, BOLD, RESET, UNDERLINE = color.red, color.blue, color.green, color.bold, color.reset, color.underline
        
        new_database_rows = []
        complete_transaction = False
        print(f"{BLUE}\nNote: Enter '{BOLD}cancel{RESET}{BLUE}' to cancel{RESET}")
        withdrawed_amount = input("Input the amount you want to withdraw: ").strip().replace(',','')
        
        
        if withdrawed_amount == "cancel" or withdrawed_amount == "Cancel":
            print(f"{RED}\nTransaction Cancelled.{RESET}")
            break
        
        elif is_float(withdrawed_amount) and '.' in withdrawed_amount: 
            withdrawed_peso, withdrawed_cent = withdrawed_amount.split(".")
            if len(withdrawed_cent) > 2:
                print(f"{RED}Please withdraw a valid amount with valid centavo values.{RESET}") 
                continue       
            
        elif not withdrawed_amount.isdigit():
            print(f"{RED}Invalid amount: Please return a valid digit{RESET}")
            continue


        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    current_value = line["user_balance"]
                    current_value, withdrawed_amount = float(current_value), float(withdrawed_amount)
                    if current_value < withdrawed_amount:
                        print(f"{RED}Please withdraw within the range of your balance.{RESET}")
                        print(f"{BLUE}Note: your current balance is: {UNDERLINE}{GREEN if int(current_value) > 0 else RED}{current_value:,.2f}{RESET}\n")
                        break
                    else:
                        user_balance_left = current_value - withdrawed_amount
                        # user_balance_left = round(user_balance_left, 2)
                        print(f"{GREEN}You have successfully withdrawed: {UNDERLINE}P{withdrawed_amount:,.2f}{RESET}")
                        complete_transaction = True
                        break
                else:
                    raise CsvError(f"An Unexpected error occured to withdrawing in the account id {user_id}")
            


        if complete_transaction:
            with open(file_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                
                for row in reader:
                    if row["user_ids"] == user_id:
                        row["user_balance"] = user_balance_left
                    new_database_rows.append(row)
                    
            with open(file_name, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_database_rows)
                
            break
                        