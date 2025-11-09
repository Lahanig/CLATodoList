# module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules', 'co'))
import modules.storage
import modules.utility 

utility = modules.utility.utility_instance
storage = modules.storage.storage_instance

def main(): 
    utility.clear_screen()

    while True:
        storage.invoke_query_method()
        storage.query()

if __name__ == "__main__": 
    main()