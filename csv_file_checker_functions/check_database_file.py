"""
    Checks for an existing user database CSV file and initializes/creates a new one if not found.

    If the file already exists, it returns a message indicating that
    the existing user database data was successfully retrieved. 

    Returns:
        str: A message indicating the status of the database file.
"""

import os
import csv

from Essentials.Terminal_colors import Colors

def check_database_file(full_file_path):
  color = Colors()
  GREEN, BOLD, RESET = color.green, color.bold, color.reset

  if os.path.exists(full_file_path):
    return f"\n{GREEN}{BOLD}(existing user database data successfully retrieved){RESET}"

  else:
    with open(full_file_path, "w", newline="") as file:
      fieldnames = ['user_ids', 'usernames', 'user_balance', 'user_passcodes']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
    return f"\n{GREEN}{BOLD}NOTICE: new user banking database has been initialized{RESET}"