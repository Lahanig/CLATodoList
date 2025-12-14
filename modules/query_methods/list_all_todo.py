import math

from modules.query_methods.base_query_method import BaseQueryMethod, query_method
from modules.storage import storage_instance as storage
from colr import Colr as C

class QueryMethod(BaseQueryMethod):
    def __init__(self):
        pass

    def render_groups(self, loop_id):
        groups = storage.get_all_groups()

        i = 0
        for group in groups:
            if group["id"] == loop_id:
                if (loop_id != 0):
                    print(" ")
                try:
                    print(f''' {C().hex(group["color"], group["text"] + f"({group["id"]+1})", rgb_mode=True)}''')
                except: 
                    print(f''' {group["text"] + f"({group["id"]+1})"}''')
            i += 1  

    def render_tasks(self, loop_id):
        tasks = storage.get_all_tasks()
        
        for task in tasks:
            if task["group_id"] == loop_id:
                if (task["is_completed"] == False):
                    try: 
                        print(f'''  {C().hex(task["color"], f"{task["in_group_id"]+1}.", rgb_mode=True)} {task["text"]}''')
                    except:
                        print(f'''  {task["in_group_id"]+1}. {task["text"]}''')
                else:
                    try:
                        print(f'''  {C().hex(task["color"], f"{task["in_group_id"]+1}.", rgb_mode=True)} \033[9m{task["text"]}\033[0m''')
                    except:
                        print(f'''  {task["in_group_id"]+1}. \033[9m{task["text"]}\033[0m''')

    @query_method
    def render(self):
        groups = storage.get_all_groups()

        if len(storage.get_all_groups()) == 0:
            print("No groups created")
        else:
            print("Todo list:")
            for i in range(len(groups)):
                self.render_groups(i)
                self.render_tasks(i)

list_all_todo = QueryMethod()