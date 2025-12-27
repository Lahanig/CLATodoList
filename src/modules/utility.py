import os

class Utility:
    def __init__(self):
        pass

    def hex_to_rgb(self, hex_code):
        """Convert a hex color string to an RGB tuple."""
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    def color_text_hex(self, hex_color, text):
        r, g, b = self.hex_to_rgb(hex_color)
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    
    def clear_screen(self):
        """Clears the terminal screen based on the operating system."""

        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')

utility_instance = Utility()