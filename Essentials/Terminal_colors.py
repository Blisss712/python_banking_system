"""
Outputs the text colors you want to use in the terminal

sample usecase:
    color = Colors()  -- initialize the class
    RED, RESET = self.red, self.reset  -- import the color you want
    print(f"{RED} This text is red.{RESET}")  -- outputs a red text
"""

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