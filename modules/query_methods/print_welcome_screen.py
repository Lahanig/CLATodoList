from modules.query_methods.query_method_decorator import query_method
from colorama import Fore, Back, Style, init

init()

@query_method
def print_welcome_screen():
    print(f'''Welcome to Kaibi {Fore.CYAN}CLATodoList{Fore.RESET}\nPrint {Fore.GREEN}help{Fore.RESET} to check command list''')