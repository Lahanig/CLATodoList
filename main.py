# module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules', 'co'))
from modules.ui import UI_instance as UI
from modules.utility import utility_instance as utility

def main(): 
    utility.clear_screen()

    while True:
        UI.invoke_query_method()
        UI.query()

if __name__ == "__main__": 
    main()