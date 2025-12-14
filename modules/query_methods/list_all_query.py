from modules.query_methods.base_query_method import BaseQueryMethod, query_method

class QueryMethod(BaseQueryMethod):
    def __init__(self):
        pass

    @query_method
    def render(self):
        print("Type this query(command) for get result\n")

        print("Query list: ")
        
        print(' "help" - print query(command) list')
        print(' "ls" - print groups and tasks list')
        print(' "clear" - clear app screen')
        print(' "welcome" - print welcome screen')
        print(' "create" - create new group/task')
        print(' "update" - create new group/task')
        print(' "remove" - remove group/task')
        print(' "exit" - exit')

list_all_query = QueryMethod()