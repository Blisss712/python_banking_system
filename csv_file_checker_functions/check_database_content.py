"""
Checks the integrity and content of the user banking database CSV file.

This function opens the 'gab's_banking_system_users.csv' file and performs
two main checks:

    1. It verifies that the CSV header (fieldnames) matches the expected
        `['user_ids', 'usernames', 'user_balance', 'user_passcodes']`.   
    2. checks if the number of columns matches the expected number and if 
       the 'user_balance' field contains a valid numeric value 
       (either an integer or a float).

Raises:
    CsvError: If the CSV header is incorrect, if a row has an invalid number
                of data parameters, or if the 'user_balance' is not a valid
                numeric format.
"""

import csv
import os

from Essentials.Custom_Errors import CsvError
from Essentials.Terminal_colors import Colors
from Essentials.is_float import is_float

def check_database_content(full_file_path):
    color = Colors()
    BOLD, RESET, RED, UNDERLINE = color.bold, color.reset, color.red, color.underline
    
    fieldnames = ['user_ids','usernames','user_balance','user_passcodes']
    number_of_columns = len(fieldnames)
    try:
        with open(full_file_path,'r',newline="") as file:
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


    except ValueError as e:
        raise ValueError(e)       
     
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    
    except IOError as e:
        raise IOError(e)   
    
    except Exception as e:
        raise Exception(e)
