from modules.query_methods.base_query_method import BaseQueryMethod, query_method
from modules.storage import storage_instance as storage

class QueryMethod(BaseQueryMethod):
    def __init__(self):
        super()

    @query_method
    def render(self):
        self.reset_default_values()
        
        is_create_new_task = True

        print("Create new task/group:")

        is_create_new_task = self.process_user_query(" Create new task or group?(default: task)(y/n): ", bool, default_value = True)

        if is_create_new_task == True:
            self.default_task["text"] = self.process_user_query(" Enter text: ")
            self.default_task["group_id"] = self.process_user_query(" Enter group id: ", int, default_value = 0)
            self.default_task["color"] = self.process_user_query(" Enter hex color(skip this field for default color): ", default_value = self.default_task["color"])

            temp_tasks = storage.get_all_tasks()

            self.default_task["id"] = len(temp_tasks)

            i = 0
            for task in temp_tasks:
                if task["group_id"] == self.default_task["group_id"]-1:
                    i = task["in_group_id"]+1
            
            self.default_task["in_group_id"] = i

            storage.create_new_task(self.default_task["id"], self.default_task["text"], self.default_task["group_id"]-1, self.default_task["in_group_id"], self.default_task["is_completed"], self.default_task["color"])
        else: 
            self.default_group["text"] = self.process_user_query(" Enter name: ")
            self.default_group["color"] = self.process_user_query(" Enter hex color(skip this field for default color): ", default_value = self.default_group["color"])

            self.default_group["id"] = len(storage.get_all_groups())

            storage.create_new_group(self.default_group["id"], self.default_group["text"], self.default_group["color"])

create_new_task_or_group = QueryMethod()