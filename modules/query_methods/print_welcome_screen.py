from modules.query_methods.query_method_decorator import query_method

@query_method
def print_welcome_screen():
    print("Welcome to Kaibi TodoList\nprint 'help' to check command list")