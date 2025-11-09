import os

class Utility:
    def __init__(self):
        pass
    
    def clear_screen(self):
        """Clears the terminal screen based on the operating system."""

        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')

utility_instance = Utility()