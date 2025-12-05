from modules.query_methods.query_method_decorator import query_method

@query_method
def list_all_query():
    print("Type this query(command) for get result\n")

    print("Query list: ")
    
    print(' "help" - print query(command) list')
    print(' "ls" - print groups and tasks list')
    print(' "clear" - clear app screen')
    print(' "welcome" - print welcome screen')
    print(' "create" - create new group/task')
    print(' "exit" - exit')