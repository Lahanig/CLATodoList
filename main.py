# module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules', 'co'))
from modules.storage import storage_instance as storage
from modules.utility import utility_instance as utility

def main(): 
    utility.clear_screen()

    while True:
        storage.invoke_query_method()
        storage.query()

if __name__ == "__main__": 
    main()