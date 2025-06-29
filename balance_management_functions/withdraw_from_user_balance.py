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


def withdraw(user_id, full_file_path):
    while True:
        color = Colors()
        RED, BLUE, GREEN, BOLD, RESET, UNDERLINE = color.red, color.blue, color.green, color.bold, color.reset, color.underline
        
        new_database_rows = []
        complete_transaction = False
        
        print(f"{BLUE}\nNote: Enter '{BOLD}{RED}cancel{RESET}{BLUE}' to cancel{RESET}")
        withdrawed_amount = input("Input the amount you want to withdraw: ").strip().replace(',','')
        
        
        if withdrawed_amount == "cancel" or withdrawed_amount == "Cancel":
            print(f"{RED}\nTransaction Cancelled.{RESET}")
            return
                
        #checks amount with centavos/decimals
        elif is_float(withdrawed_amount) and '.' in withdrawed_amount: 
            withdrawed_peso, withdrawed_cent = withdrawed_amount.split(".")
        
            if not withdrawed_peso.isdigit() or not withdrawed_cent.isdigit(): 
                print(f"{RED}Please enter a digit before/after the decimal")
                print(f"Example: '{BOLD}2.0{RESET}{RED}', '{BOLD}0.2{RESET}{RED}'")
                continue

            elif len(withdrawed_cent) > 2:
                print(f"{RED}{BOLD}Error: {RESET}{RED}Invalid length of centavo digits.{RESET}")
                print(f"{RED}Please withdraw a valid amount with valid centavo values.{RESET}") 
                continue      
            
            elif int(withdrawed_peso) == 0 and int(withdrawed_cent) == 0:
                print(f"{RED}Please deposit a valid amount with valid centavo values.{RESET}")
                continue 
        
        # checks amount with whole numbers
        elif not withdrawed_amount.isdigit():
            print(f"{RED}Invalid amount: Please enter a valid {BOLD}digit/value{RESET}")
            continue

        elif int(withdrawed_amount) == 0:
            print(f"{RED}Please withdraw a valid amount with valid centavo values.{RESET}")
            continue


        try:
            with open(full_file_path, "r", newline="") as file:
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
                            print(f"{GREEN}You have successfully withdrawed: {UNDERLINE}P{withdrawed_amount:,.2f}{RESET}")
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

                        