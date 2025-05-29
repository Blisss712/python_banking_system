"""
    Displays:
        - The user navigation in the account management section.
        
"""
from Essentials.Terminal_colors import Colors
    
def display_account_management_options():
    color = Colors()
    BLUE, RESET = color.blue, color.reset
    print(f"{BLUE}\n\nHow would you like to manage your acccount?{RESET}")
    print("1. Edit my Full Name")
    print("2. Edit my Password")
    print("3. Delete my Account")
    print("4. Exit\n")