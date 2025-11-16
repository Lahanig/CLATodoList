import math

from modules.query_methods.query_method_decorator import query_method
from modules.storage import storage_instance as storage
from colr import Colr as C

class Render:
    def __init__(self):
        pass

    def render_groups(self, loop_id):
        groups = storage.get_all_groups()

        for group in groups:
            if group["id"] == loop_id:
                if (loop_id != 0):
                    print(" ")
                print(f''' {C().hex(group["color"], group["text"], rgb_mode=True)}''')

    def render_tasks(self, loop_id):
        tasks = storage.get_all_tasks()
        
        i = 0
        for task in tasks:
            if task["group_id"] == loop_id:
                if (task["is_completed"] == False):
                    print(f'''  {i+1}. {task["text"]}''')
                else:
                    print(f'''  {i+1}. \033[9m{task["text"]}\033[0m''')
                i += 1

    @query_method
    def list_all_todo(self):
        groups = storage.get_all_groups()

        print("Todo list:")
        for i in range(len(groups)):
            self.render_groups(i)
            self.render_tasks(i)

render = Render()