"""
Displays: 
    - the full name of a specific user.
    - ID number of a specific user.

Raises:
    CsvError: If an unexpected error occurs during file processing.
"""

import csv

from Essentials.Terminal_colors import Colors
from Essentials.Custom_Errors import CsvError

def display_user_information(user_id, full_file_path):
    color = Colors()
    BLUE, RESET, YELLOW, UNDERLINE = color.blue, color.reset, color.yellow, color.underline
    
    try:
        with open(full_file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row["user_ids"] == user_id:
                    print(f"\n\n{BLUE}Full name: {YELLOW}{UNDERLINE}{row['usernames']}{RESET}")
                    print(f"{BLUE}Id number: {YELLOW}{UNDERLINE}{user_id}{RESET}\n")


    except ValueError as e:
        raise ValueError(e)       
     
    except FileNotFoundError as e:
        raise FileNotFoundError(e)
    
    except IOError as e:
        raise IOError(e)   
    
    except Exception as e:
        raise Exception(e)
        