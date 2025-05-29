import csv

from Essentials.Terminal_colors import Colors

def change_user_password(user_id, full_file_path):
    new_database_rows = []

    color = Colors()
    RED, BLUE, GREEN, BOLD, RESET, UNDERLINE = color.red, color.blue, color.green, color.bold, color.reset, color.underline
        

    while True:
        print(f"{BLUE}\nNote: Enter '{RED}{BOLD}0{RESET}{BLUE}' to cancel{RESET}")
        new_passcode = input("Enter your new password: ")
        confirm_new_passcode = input("Confirm your password: ")
        
        if new_passcode =="0" or confirm_new_passcode == "0":
            return False
        elif new_passcode != confirm_new_passcode:
            print(f"{RED}Passwords do not match, please re-enter your password.\n{RESET}")
            continue
        
        try:
            with open(full_file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for line in reader:
                    if line["user_ids"] == user_id:
                        line["user_passcodes"] = new_passcode
                        print(f"{GREEN}\nPassword changed successfully!{RESET}")
                    new_database_rows.append(line)
                    
            with open(full_file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_database_rows)
                return 
            
        except FileNotFoundError as e:
            raise FileNotFoundError(e)
        except Exception as e:
            raise Exception(e)