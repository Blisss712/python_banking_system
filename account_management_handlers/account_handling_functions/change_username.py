import csv

# from account_management_handlers.handle_account_functions.Terminal_colors import Colors
from Essentials.Terminal_colors import Colors

def change_username(user_id, full_file_path):
    new_database_rows = []

    color = Colors()
    RED, BLUE, GREEN, BOLD, RESET = color.red, color.blue, color.green, color.bold, color.reset
        

    while True:
        print(f"{BLUE}\nNote: Enter '{RED}{BOLD}0{RESET}{BLUE}' to cancel{RESET}")
    
        first_name = input(f"Enter your {BOLD}first{RESET} name: ").strip()
        if first_name == "0":
            return False
        middle_name = input(f"\nEnter your {BOLD}middle{RESET} name: ").strip()
        if middle_name == "0":
            return False
        last_name = input(f"\nEnter your {BOLD}last{RESET} name: ").strip()
        if last_name == "0":
            return False
        
        if not first_name.replace(" ","").isalpha():
            print(f"{RED}\nThere was a problem with the first name you entered.{RESET}")
            print(f"{RED}Please do not include {BOLD}special characters or digits{RESET}{RED} to your name and try again.{RESET}")
            continue
        elif not middle_name.replace(" ", "").isalpha():
            print(f"{RED}\nThere was a problem with the middle name you entered.{RESET}")
            print(f"{RED}Please do not include {BOLD}special characters or digits{RESET}{RED} to your name and try again.{RESET}")
            continue
        elif not last_name.replace(" ", "").isalpha():
            print(f"{RED}\nThere was a problem with the last name you entered.{RESET}")
            print(f"{RED}Please do not include {BOLD}special characters or digits{RESET}{RED} to your name and try again.{RESET}")
            continue
        
        
        middle_initial = middle_name[0] + "."
        new_username = first_name.capitalize() + " " + middle_initial.capitalize() + " " + last_name.capitalize()
        
        try:
            with open(full_file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for line in reader:
                    if line["user_ids"] == user_id:
                        line["usernames"] = new_username
                        print(f"{GREEN}User's full name successfully changed to {BOLD}{line["usernames"]}{RESET}{GREEN}!{RESET}")
                    new_database_rows.append(line)
                    
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