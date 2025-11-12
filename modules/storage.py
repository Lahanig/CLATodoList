from colorama import Fore, Back, Style, init

init()

class Storage:
    def __init__(self):
        pass
    
    def get_all_groups(self):
        return [{"id": 0, "text": "Важно", "color": Fore.RED}, {"id": 1, "text": "Менее важно", "color": Fore.YELLOW}, {"id": 2, "text": "Не забыть", "color": Fore.GREEN}]

    def get_all_tasks(self):
        return [{"id": 0, "text": "Сделать рендер туду из бд aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "group_id": 0, "is_completed": False}, {"id": 1, "text": "Тыкать контент гач aaaaaaaaaaaaaaaa", "group_id": 1, "is_completed": False}, {"id": 2, "text": "Покакать", "group_id": 2, "is_completed": True}, {"id": 3, "text": "Сделать рендер туду из бд", "group_id": 2, "is_completed": False}]

storage_instance = Storage()