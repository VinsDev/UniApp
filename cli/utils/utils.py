import re
from colors.text_colors import *

class Utils:
    EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    PASSWORD_REGEX = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$"

    def printInvalidEntry():
        print(RED + "Invalid choice. Please select again." + RESET)
