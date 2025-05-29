"""
Displays:
    - the balance of a specific user from the banking system's CSV file.

Raises:
    CsvError:
        - If the 'user_balance' in the CSV is not a valid float or integer,
            or has an invalid format (e.g., too many decimal points).
        - If the provided user_id is not found in the CSV file.
"""

import csv

from Essentials.Terminal_colors import Colors
from Essentials.is_float import is_float
from Essentials.Custom_Errors import CsvError

def display_balance(user_id, full_file_path):
    color = Colors()
    BLUE, GREEN, UNDERLINE, RESET = color.blue, color.green, color.underline, color.reset
    
    try:
        with open(full_file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            user_exists = False
            
            for row in reader:
                if row["user_ids"] == user_id:
                    current_balance = row["user_balance"]
                    
                    if is_float(current_balance) and ('.' in current_balance):
                        balance_list = current_balance.split(".")
                        peso, centavo = balance_list

                        if peso.isdigit() and centavo.isdigit():
                            print(f"\n\n{BLUE}{row["usernames"]}'s balance: {RESET}")
                            print(f"{GREEN}{UNDERLINE}P{float(current_balance):,.2f}{RESET}\n")
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
                raise CsvError("Error in displaying balance: User doesn't exist")
            
            
    except ValueError as e:
        raise ValueError(e)       
     
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    
    except IOError as e:
        raise IOError(e)   
    
    except Exception as e:
        raise Exception(e)
        
