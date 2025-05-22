import csv
import os


class CsvError(Exception):
    pass

class FileError(Exception):
    pass

class Colors:
    def __init__(self):
        self.red = "\033[31m"
        self.green = "\033[32m"
        self.reset = "\033[0m"
        self.bold = "\033[1m"
        self.underline = "\033[4m"
        self.faded = "\033[2m"
        self.blue = "\033[34m"
        self.yellow = "\033[33m"
        self.bblue = "\033[94m" # bright blue color
        
class Options:
    def __init__(self):
        self.yes = ["YES","Yes","yes", "yEs", "YeS", "yeS","y","Y"]
        self.no = ["No","nO","NO","no","N","n"]
        

def is_float(s):
    """
    Checks if a string can be successfully converted to a float.

    Args:
    s: The string to check.

    Returns:
    bool: True if the string can be converted to a float, False otherwise.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def deposit(user_id):
    file_name = "gab's_banking_system_users.csv"
    
    while True:
        color = Colors()
        RED, GREEN, RESET, UNDERLINE = color.red, color.green, color.reset, color.underline
        
        new_database_rows = []
        complete_transaction = False
        deposit_amount = input("\nInput the amount you want to deposit: ").strip().replace(',','')
        if deposit_amount == "cancel" or deposit_amount == "Cancel":
            print(f"{RED}\nTransaction Cancelled.{RESET}")
            break
        
        if is_float(deposit_amount) and '.' in deposit_amount:
            deposit_peso, deposit_cent = deposit_amount.split(".")
            if len(deposit_cent) > 2:
                print(f"{RED}Please deposit a valid amount no lesser than one centavo.{RESET}") 
                continue
                
        elif not deposit_amount.isdigit():
            print(f"{RED}Invalid amount: Please return a valid digit/value{RESET}")
            continue

        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    current_value = line["user_balance"]
                    current_value, deposit_amount = float(current_value), float(deposit_amount)

                    user_balance_left = current_value + deposit_amount
                    print(f"{GREEN}You have successfully depositted: {UNDERLINE}P{deposit_amount:.2f}{RESET}")
                    complete_transaction = True
                    break
                
                else:
                    raise CsvError(f"An Unexpected error occured to withdrawing in the account id {user_id}")
                
        if complete_transaction:
            with open(file_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                
                for row in reader:
                    if row["user_ids"] == user_id:
                        row["user_balance"] = user_balance_left
                    new_database_rows.append(row)
                    
            with open(file_name, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_database_rows)
                
            break
                
def withdraw(user_id):
    file_name = "gab's_banking_system_users.csv"
    
    while True:
        color = Colors()
        RED, GREEN, RESET, UNDERLINE = color.red, color.green, color.reset, color.underline
        
        new_database_rows = []
        complete_transaction = False
        withdrawed_amount = input("\nInput the amount you want to withdraw: ").strip().replace(',','')
        
        if withdrawed_amount == "cancel" or withdrawed_amount == "Cancel":
            print(f"{RED}\nTransaction Cancelled.{RESET}")
            break
        if is_float(withdrawed_amount) and '.' in withdrawed_amount: 
            withdrawed_peso, withdrawed_cent = withdrawed_amount.split(".")
            if len(withdrawed_cent) > 2:
                print(f"{RED}Please withdraw a valid amount no lesser than one centavo.{RESET}") 
                continue
                
        elif not withdrawed_amount.isdigit():
            print(f"{RED}Invalid amount: Please return a valid digit{RESET}")
            continue

        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    current_value = line["user_balance"]
                    current_value, withdrawed_amount = float(current_value), float(withdrawed_amount)
                    if current_value < withdrawed_amount:
                        print(f"{RED}Please withdraw within the range of your balance.{RESET}")
                        print(f"Note: your current balance is: {UNDERLINE}{current_value}{RESET}\n")
                        break
                    else:
                        user_balance_left = current_value - withdrawed_amount
  
                        print(f"{GREEN}You have successfully withdrawed: {UNDERLINE}P{withdrawed_amount:.2f}{RESET}")
                        complete_transaction = True
                        break
                else:
                    raise CsvError(f"An Unexpected error occured to withdrawing in the account id {user_id}")
            


        if complete_transaction:
            with open(file_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                
                for row in reader:
                    if row["user_ids"] == user_id:
                        row["user_balance"] = user_balance_left
                    new_database_rows.append(row)
                    
            with open(file_name, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(new_database_rows)
                
            break
                        


def display_balance(user_id):
    color = Colors()
    UNDERLINE, RESET = color.underline, color.reset
    file_name = "gab's_banking_system_users.csv"
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        user_exists = False
        
        for row in reader:
            if row["user_ids"] == user_id:
                current_balance = row["user_balance"]
                
                if is_float(current_balance) and ('.' in current_balance):
                    balance_list = current_balance.split(".")
                    peso, centavo = balance_list

                    if peso.isdigit() and centavo.isdigit():
                        print(f"\n{row["usernames"]}'s balance: ")
                        print(f"{UNDERLINE}P{int(peso):,}.{centavo}{RESET}")
                        user_exists = True
                        break
                    elif len(balance_list) > 3:
                        raise CsvError("Error in displaying balance: invalid centavo values") 
                    else:
                        raise CsvError("Error in displaying balance: invalid peso and centavo values")
                    
                elif row["user_balance"].isdigit():
                    print(f"\n{row["usernames"]}'s balance: ")
                    print(f"{UNDERLINE}P{int(current_balance):,.2f}{RESET}")
                    user_exists = True
                    break

        if not user_exists:
            raise CsvError("Error in displaying balance: invalid centavo values")



def display_user_information(user_id):
    color = Colors()
    BLUE, RESET = color.blue, color.reset
    file_name = "gab's_banking_system_users.csv"
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        
        try:
            for row in reader:
                if row["user_ids"] == user_id:
                    full_name = row["usernames"]
                    print(f"\nFull name: {BLUE}{full_name.capitalize()}{RESET}")
                    print(f"Id number: {BLUE}{user_id}{RESET}")
        except Exception as e:
            raise CsvError(e)



def prompt_and_execute_user_choice(user_id):
    color = Colors()
    RED, BOLD, RESET = color.red, color.bold, color.reset
    while True:
        display_user_navigation(user_id)
        user_choice = input("\nEnter your chosen option here: ")
        if user_choice == "1":
            withdraw(user_id)
        elif user_choice == "2":
            deposit(user_id)
        elif user_choice == "3":
            display_balance(user_id)
        elif user_choice == "4":
            display_user_information(user_id)
        elif user_choice == "5":
            return
        else:
            print(f"{RED}your input '{BOLD}{user_choice}{RESET}{RED}' is not in the navigation list, please enter a valid value{RESET}")

        
        
def display_user_navigation(user_id):
    color = Colors()
    RED, YELLOW, BLUE, RESET = color.red, color.yellow, color.blue, color.reset
    file_name = "gab's_banking_system_users.csv"
    try:
        id_not_found = True
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    print(f"\n{YELLOW}Hello {line['usernames'].capitalize()}!{RESET}")
                    print(f"{BLUE}Enter any number to navigate for your account.{RESET}")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Display balance")
                    print("4. Display User Information")
                    print("5. Log-out")
                    id_not_found = False
            
            
            if id_not_found:
                raise CsvError(f"{RED}Something went wrong the to user id.{RESET}")     
        
    except FileNotFoundError as e:
        print("{RED}File Error in display_user_navigation:{RESET}")
        raise CsvError(e)

# Always returning false allows forced log-in after the signing up process.
def create_new_account(file_name: str) -> False:
    try:
        color = Colors()
        options = Options()
        RED, BOLD, RESET = color.red, color.bold, color.reset
        while True:
            id_exists = False
            back_to_login = False
            print(f"Type '{BOLD}quit{RESET}' to any options to cancel.\n")
            username = input("Enter your full name: ").strip()
            user_id = input("Enter your unique user_id (digits only): ").strip()
            
            if username == "quit" or user_id == "quit":
                return False
            
            if not user_id.isdigit():
                raise ValueError("Please provide the necessary inputs for the user_id")
            

            with open(file_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                for line in reader:
                    if line["usernames"] == username:
                        if line["user_ids"] == user_id:
                            print(f"\nUser '{username}' with the id [{user_id}] already exists.")
                            confirm = input("Is this you? (yes/no): ")
                            if confirm in options.yes:
                                print("\nPlease return to log-in and enter your account")
                                back_to_login = True
                                break
                            elif confirm in options.no:
                                print("\nThe given id already exists. Please create a different user id!")
                                id_exists = True
                                break
                            else:
                                raise ValueError("Please provide the necessary inputs for the user's options")
                    elif line["user_ids"] == user_id:
                        print("\nThe given id already exists. Please create a different user id!")
                        id_exists = True
                        break

            if id_exists:
                continue
            elif back_to_login:
                return False
            else:
                break
                
                    
        while True: 
            passcode = input("Enter your new password: ")
            confirm_passcode = input("Confirm your password: ")
            
            if passcode =="quit" or confirm_passcode == "quit":
                return False
            elif passcode != confirm_passcode:
                print("Passwords do not match, please re-enter your password.")
                continue
            
            try:
                with open(file_name, "a", newline="") as file:
                    fieldnames = ['user_ids','usernames','user_balance','user_passcodes']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow({"user_ids":user_id, "usernames": username, "user_balance":0, "user_passcodes":passcode})
                print(f"Successfully created user {username}")
                return False
            except IOError as e:
                print("Something went wrong when adding user to the csv")
                raise CsvError(e)
            except FileNotFoundError as e:
                print("Something went wrong when adding user to the csv") 
                raise FileNotFoundError(e)   
            except Exception as e:
                print("Unexpected Error:",e)          
                            
    except ValueError as e:
        print(f"\n{RED}An Error Occured: {e}{RESET}")
    except Exception as e:
        print(f"\n{RED}An Unexpected Error Occured: {e}{RESET}")

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
        
        # option = int(input("user database doesn't exist, do you want to make a new one to continue? (Yes/No) "))
        # if option == "no" or option == "No":

# returns user_id or a false value
def verify_user(file_name: str):
    
    color = Colors()
    RED, BOLD, GREEN, RESET = color.red, color.bold, color.green, color.reset, 
    user_id = input("Enter your user id: ").strip()
    with open(file_name, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["user_ids"] == user_id:
                passcode = input("Enter your password: ")
                attempts = 3
                while True:
                    if row["user_passcodes"] == passcode:
                        print(f"\n{GREEN}You have successfully signed in to your account!{RESET}")
                        return user_id
                    elif attempts >= 1:
                        print(f"{RED}{BOLD}Invalid password:{RESET}{RED}  you have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.{RESET}")
                        passcode = input("Enter your password: ")
                        attempts -= 1
                    else:
                        print(f"\n{BOLD}{RED}Login Failed{RESET}")
                        print(f"{RED}(Please enter the correct password.){RESET}")
                        return False
     
        print(f"\n{RED}{BOLD}Cannot find the user with user_id: {user_id}{RESET}")
        return False
    

#returns user_id or a false value
def handle_authentication(user_option: str):
    current_path = os.getcwd()
    file_name = "gab's_banking_system_users.csv"
    
    if os.path.exists(current_path+"\\"+ file_name):
        if user_option == 1:
            authenticated_id = verify_user(file_name)
            return authenticated_id
        elif user_option == 2:
            forced_login = create_new_account(file_name) # always returns false 
            return forced_login
    else:
        raise FileNotFoundError("User database has been edited/deleted")
    
        
def main():
    
    try:
        color = Colors()
        GREEN, RED, BOLD, RESET = color.green, color.red, color.bold, color.reset
        print(check_database_file())
        print(f"\n\n\n{GREEN}Welcome to Gab's Banking system!{RESET}")
        while True:
            check_database_file()
            check_database_content()
            print(f"\n\nEnter the following numbers to navigate:")
            print("1. Login to your account")
            print("2. Sign up to your account")
            print("3. Exit Program\n")
            
            user_authentication_option = int(input("Input your chosen option here: ").strip())
            
            if user_authentication_option == 3:
                print(f"{GREEN}{BOLD}\nThank you for using Gab's banking system!\n{RESET}")
                print(f"{RED}Exitting program...{RESET}")
                break
            
            authenticated_id = handle_authentication(user_authentication_option) # returns a string
        
            # goes back to user authentication if the string value is false -- (when continue is triggered by the else statement)
            if authenticated_id:
                prompt_and_execute_user_choice(authenticated_id)
            else:
                continue
    
    except ValueError as e:
        print(f"{BOLD}{RED}\nError:{RESET}{RED} Please enter a valid input and try again\n{RESET}")
        
    except FileNotFoundError as e:
        print("Error:", e)
        return
    
    except CsvError as e:
        print(f"{BOLD}{RED}Error in the csv file: {RESET}{RED} {e} {RESET}")
        print(f"{RED}Please undo any changes to the banking system database file.\n{RESET}")
        
    except Exception as e:
        print("Unexpected error:", e)
        
if __name__ == "__main__":
    main()
    # withdraw("1")