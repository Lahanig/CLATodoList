from modules.query_methods.query_method_decorator import query_method
from modules.storage import storage_instance as storage
from colorama import Fore, Back, Style, init
import math

init()

class Render:
    def __init__(self):
        pass

    def render_groups(self, loop_id):
        groups = storage.get_all_groups()

        for group in groups:
            if group["id"] == loop_id:
                if (loop_id != 0):
                    print(" ")
                print(f'''{group["color"]}{group["text"]}{Fore.RESET}''')

    def render_tasks(self, loop_id):
        tasks = storage.get_all_tasks()
        
        i = 0
        for task in tasks:
            if task["group_id"] == loop_id:
                temp_str = f'''{i+1}. {task["text"]}'''

                if (task["is_completed"] == False):
                    print(f''' {temp_str}''')
                else:
                    print(f'''\033[9;30m {temp_str}\033[0m''')
                i += 1

    @query_method
    def list_all_todo(self):
        groups = storage.get_all_groups()

        for i in range(len(groups)):
            self.render_groups(i)
            self.render_tasks(i)

render = Render()