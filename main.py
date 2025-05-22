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

def withdraw(user_id):
    file_name = "gab's_banking_system_users.csv"
    withdrawed_amount = input("How much do you want? ")
    
    if is_float(withdrawed_amount) and '.' in withdrawed_amount: 
        withdrawed_peso, withdrawed_cent = withdrawed_amount.split(".")
        if len(withdrawed_cent) > 0:
            print("Please withdraw a valid amount no lesser than one centavo.") 
    elif '.' not in withdrawed_amount:
        withdrawed_peso = withdrawed_amount
    else:
        print("Invalid amount: please try again.")
    with open(file_name, "r", newline="") as file:
        
        reader = csv.DictReader(file)
        for line in reader:
                if line["user_ids"] == user_id:
                    current_value = line["user_ids"]
                    


def display_balance():
    pass

def deposit():
    pass

def display_user_information():
    pass

def prompt_and_execute_user_choice(user_id):
    color = Colors()
    RED, BOLD, RESET = color.red, color.bold, color.reset
    while True:
        user_choice = input("Enter your chosen option here: ")
        if user_choice == 1:
            withdraw(user_id)
        elif user_choice == 2:
            deposit(user_id)
        elif user_choice == 3:
            display_balance(user_id)
        elif user_choice == 4:
            display_user_information(user_id)
        elif user_choice == 5:
            return
        else:
            print(f"{RED}your input '{BOLD}{user_choice}{RESET}{RED}' is not in the navigation list, please enter a valid value{RESET}")

        
        
def display_user_navigation(user_id):
    color = Colors()
    RED, RESET = color.red, color.reset
    file_name = "gab's_banking_system_users.csv"
    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["user_ids"] == user_id:
                    print(f"Hello {line['usernames']}!")
                    print(f"Enter any number to navigate for your account.")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Display balance")
                    print("4. Display User Information")
                    print("5. Log-out")
                else:
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
                elif not balance.isdigit():
                    raise CsvError("Error in the user dataset, invalid balance value.")
                                
    
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
    RED, BOLD, GREEN, RESET = color.red, color.bold, color.green, color.reset
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
                        print(f"Invalid password, you have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
                        passcode = input("Enter your password: ")
                        attempts -= 1
                    else:
                        print(f"\n{BOLD}{RED}Login Failed{RESET}")
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
                display_user_navigation(authenticated_id)
                prompt_and_execute_user_choice(authenticated_id)
            else:
                continue
    
    except ValueError as e:
        print(f"{BOLD}{RED}Error:{RESET}", e)
        
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