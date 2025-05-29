import csv

# from account_management_handlers.handle_account_functions.Terminal_colors import Colors
from Essentials.Terminal_colors import Colors
from Essentials.User_options import Options

def delete_user_account(user_id, full_file_path):
    new_database_rows = []

    color = Colors()
    options = Options()
    RED, BLUE, BOLD, RESET = color.red, color.blue, color.bold, color.reset
        

    while True:
        
        print(f"{RED}\nWarning: this change is {BOLD}irreversible{RESET}{RED}.{RESET}")
        user_confimation = input("Are you sure you want to delete your own account? (yes/no): ").strip()
        
        account_deleted = False
        
        if user_confimation in options.yes:
            pass
        elif user_confimation in options.no:
            print(f"{BLUE}\nUser deletion cancelled.{RESET}")
            return
        else:
            print(f"{BLUE}\nPlease Enter a valid input.{RESET}")
            continue
        
        try:
            with open(full_file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for line in reader:
                    if line["user_ids"] == user_id:
                        print(f"{RED}\nUser {BOLD}{line["usernames"]}{RESET}{RED} with id {BOLD}{line["user_ids"]}{RESET}{RED} is successfully removed from the Banking System!{RESET}")
                    else:
                        new_database_rows.append(line)
                    
            with open(full_file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_database_rows)
                account_deleted = True
                return account_deleted
            
            
            
        except ValueError as e:
            raise ValueError(e)         
        
        except FileNotFoundError as e:
            raise FileNotFoundError(e)
        
        except IOError as e:
            raise IOError(e)   
        
        except Exception as e:
            raise Exception(e)

