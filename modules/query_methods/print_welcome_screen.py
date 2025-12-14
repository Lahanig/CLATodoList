from modules.query_methods.base_query_method import BaseQueryMethod, query_method
from colr import Colr as C

class QueryMethod(BaseQueryMethod):
    def __init__(self):
        pass

    @query_method
    def render(self):
        print(f'''Welcome to Kaibi {C().hex('00aaff', 'CLATodoList', rgb_mode=True)}\nPrint {C().hex('00ff00', 'help', rgb_mode=True)} to check query(command) list''')

print_welcome_screen = QueryMethod()