from modules.query_methods.query_method_decorator import query_method
from colorama import Fore, Back, Style, init

init()

@query_method
def list_all_todo():
    print(f'''|{Fore.RED}Важно                    {Fore.RESET}|{Fore.YELLOW}Менее важно       {Fore.RESET}|{Fore.GREEN}Не забыть{Fore.RESET}       |''')
    print(f'''|{Fore.RESET}Сделать рендер туду из бд{Fore.RESET}|{Fore.RESET}Тыкать контент гач{Fore.RESET}|{Fore.RESET}Покакать{Fore.RESET}        |''')