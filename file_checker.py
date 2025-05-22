"""
Checks the integrity and content of the user banking database CSV file.

This function opens the 'gab's_banking_system_users.csv' file and performs
two main checks:
    1. It verifies that the CSV header (fieldnames) matches the expected
        `['user_ids', 'usernames', 'user_balance', 'user_passcodes']`.
    2. For each row in the CSV, it checks if the number of columns matches
        the expected number and if the 'user_balance' field contains a
        valid numeric value (either an integer or a float).


If any of these checks fail, a `CsvError` is raised, indicating data corruption
or an unexpected format within the CSV file. If all checks pass, the function
completes silently.

Raises:
    CsvError: If the CSV header is incorrect, if a row has an invalid number
                of data parameters, or if the 'user_balance' is not a valid
                numeric format.
"""

import csv
import os

from Custom_Errors import CsvError
from Terminal_colors import Colors
from is_float import is_float

def check_database_content():
    color = Colors()
    BOLD, RESET, RED, UNDERLINE = color.bold, color.reset, color.red, color.underline
    
    fieldnames = ['user_ids','usernames','user_balance','user_passcodes']
    number_of_columns = len(fieldnames)
    file_name = "gab's_banking_system_users.csv"
    with open(file_name,'r',newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != fieldnames:
            raise CsvError("Error in the fieldnames(header) data")
        
        else:
            for line in reader:
                balance = line["user_balance"]
                if len(line) != number_of_columns:
                    raise CsvError("Error in the user dataset, invalid number of user data parameters.")
                elif is_float(balance) and '.' in balance:
                    return
                elif not balance.isdigit():
                    raise CsvError(f"Error in the user dataset, invalid {UNDERLINE}{BOLD}balance{RESET}{RED} value.")
                                
    
def check_database_file():
    color = Colors()
    GREEN, BOLD, RESET = color.green, color.bold, color.reset
    current_path = os.getcwd()
    file_name = "gab's_banking_system_users.csv"
    # print(current_path+"\\"+ file_name)
    
    if os.path.exists(current_path+"\\"+ file_name):
        return(f"\n{GREEN}{BOLD}(existing user database data successfully retrieved){RESET}")
        
    else:
        with open(file_name,"w",newline="") as file:
            fieldnames = ['user_ids','usernames','user_balance','user_passcodes']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
        return(f"\n{GREEN}{BOLD}NOTICE: new user banking database has been initialized{RESET}")
        