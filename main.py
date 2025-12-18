# module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules', 'co'))
import sys
import readline
import os
import atexit

from modules.storage import storage_instance as storage
from modules.ui import UI_instance as UI
from modules.utility import utility_instance as utility

history_file = os.path.join(storage.current_home_path, '.app_history')

def save_history():
    """Saves the current session's history to a file."""
    try:
        readline.write_history_file(history_file)
    except IOError:
        pass
        # print(f"Warning: Could not write history file to {history_file}")

def load_history():
    """Loads history from a file if it exists."""
    if os.path.exists(history_file):
        try:
            readline.read_history_file(history_file)
        except IOError:
            print(f"Warning: Could not read history file from {history_file}")

# Load the history when the script starts
load_history()

# Register the save_history function to be called automatically when the script exits
atexit.register(save_history)

def main(): 
    utility.clear_screen()

    while True:
        try:
            UI.invoke_query_method()
            UI.query()
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__": 
    if len(sys.argv) > 1 and sys.argv[1].lower() == "dev":
        storage.is_dev_mode = True
        main() 
    else:
        main()    