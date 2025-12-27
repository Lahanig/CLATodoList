from modules.query_methods.base_query_method import BaseQueryMethod, query_method
from modules.utility import utility_instance as utility

class QueryMethod(BaseQueryMethod):
    def __init__(self):
        pass

    @query_method
    def render(self):
        print(f'''Welcome to Kaibi {utility.color_text_hex('00aaff', 'CLATodoList')}\nPrint {utility.color_text_hex('00ff00', 'help')} to check query(command) list''')

print_welcome_screen = QueryMethod()