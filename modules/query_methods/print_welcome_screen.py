from modules.query_methods.query_method_decorator import query_method
from colr import Colr as C

@query_method
def print_welcome_screen():
    print(f'''Welcome to Kaibi {C().hex('00aaff', 'CLATodoList', rgb_mode=True)}\nPrint {C().hex('00ff00', 'help', rgb_mode=True)} to check command list''')