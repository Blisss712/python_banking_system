"""
Includes the process of writting the csv file if transaction is successful

Args:
    user_id (str): The ID of the user performing the withdrawal.

Raises:
    CsvError: If an unexpected error occurs while trying to find the user
"""

import csv
 
from Essentials.Terminal_colors import Colors
from Essentials.is_float import is_float


def deposit(user_id, full_file_path):
    while True:
        color = Colors()
        RED, GREEN, BLUE, BOLD, RESET, UNDERLINE = color.red, color.green, color.blue, color.bold, color.reset, color.underline
        
        new_database_rows = []
        complete_transaction = False
        print(f"{BLUE}\nNote: Enter '{BOLD}{RED}cancel{RESET}{BLUE}' to cancel{RESET}")
        deposit_amount = input("Input the amount you want to deposit: ").strip().replace(',','')
        
        if deposit_amount == "cancel" or deposit_amount == "Cancel":
            print(f"{RED}\nTransaction Cancelled.{RESET}")
            break
        
            
        #checks amount with centavos/decimals
        elif is_float(deposit_amount) and '.' in deposit_amount:
            deposit_peso, deposit_cent = deposit_amount.split(".")
        
            if not deposit_peso.isdigit() or not deposit_cent.isdigit(): 
                print(f"{RED}Please enter a digit before/after the decimal")
                print(f"Example: '{BOLD}2.0{RESET}{RED}', '{BOLD}0.2{RESET}{RED}'")
                continue

            elif len(deposit_cent) > 2:
                print(f"{RED}{BOLD}Error: {RESET}{RED}Invalid length of centavo digits.{RESET}")
                print(f"{RED}Please withdraw a valid amount with valid centavo values.{RESET}") 
                continue      
            
            elif int(deposit_peso) == 0 and int(deposit_cent) == 0:
                print(f"{RED}Please deposit a valid amount with valid centavo values.{RESET}")
                continue 
            
        
        # checks amount with whole numbers
        elif not deposit_amount.isdigit():  
            print(f"{RED}Invalid amount: Please enter a valid {BOLD}digit/value{RESET}")
            continue

        elif int(deposit_amount) == 0:
            print(f"{RED}Please deposit a valid amount with valid centavo values.{RESET}")
            continue
        
        
        try:
            with open(full_file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                for line in reader:
                    if line["user_ids"] == user_id:
                        current_value = line["user_balance"]
                        current_value, deposit_amount = float(current_value), float(deposit_amount)

                        user_balance_left = current_value + deposit_amount
                        print(f"{GREEN}You have successfully depositted: {UNDERLINE}P{deposit_amount:,.2f}{RESET}")
                        complete_transaction = True
                        break
                    
                    
                    
        except ValueError as e:
            raise ValueError(e)       

        except FileNotFoundError as e:
            raise FileNotFoundError(e)
        
        except IOError as e:
            raise IOError(e)   
        
        except Exception as e:
            raise Exception(e)
        
                    
                    
        if complete_transaction:
            try:
                with open(full_file_path, "r", newline="") as file:
                    reader = csv.DictReader(file)
                    fieldnames = reader.fieldnames
                    
                    for row in reader:
                        if row["user_ids"] == user_id:
                            row["user_balance"] = user_balance_left
                        new_database_rows.append(row)
                        
                with open(full_file_path, "w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(new_database_rows)
                    return
                
                
                
            except ValueError as e:
                raise ValueError(e)       
            
            except FileNotFoundError as e:
                raise FileNotFoundError(e)
            
            except IOError as e:
                raise IOError(e)   
            
            except Exception as e:
                raise Exception(e)
