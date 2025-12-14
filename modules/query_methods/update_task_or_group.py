from modules.query_methods.base_query_method import BaseQueryMethod, query_method
from modules.storage import storage_instance as storage

class QueryMethod(BaseQueryMethod):
    def __init__(self):
        super()

    @query_method
    def render(self):
        self.reset_default_values()

        is_update_task = True

        print("Update data in task/group:")

        is_update_task = self.process_user_query(" Update task or group?(default: task)(y/n): ", bool, default_value = True)

        if is_update_task == True:
            tasks = storage.get_all_tasks()
            
            temp_task_group_id = self.process_user_query(" Enter task group id: ", int) - 1
            temp_task_in_group_id = self.process_user_query(" Enter task id in group: ", int) - 1

            for task in tasks:
                if task["group_id"] == temp_task_group_id and task["in_group_id"] == temp_task_in_group_id:
                    self.default_task = {"id": task["id"], "text": task["text"], "group_id": task["group_id"], "in_group_id": task["in_group_id"], "is_completed": task["is_completed"], "color": task["color"]}

            self.default_task["text"] = self.process_user_query(" Enter new text(skip this field for save old data): ", default_value = self.default_task["text"])
            self.default_task["group_id"] = self.process_user_query(" Enter task new group id(skip this field for save old data): ", int, default_value = self.default_task["group_id"] + 1) - 1 
            # temp_task["in_group_id"] = int(input(" Enter new task id in group(skip this field for save old data): ")) or temp_task["in_group_id"]            
            self.default_task["is_completed"] = self.process_user_query(" Complete task?(y/n)(default: n): ", bool, False)

            self.default_task["color"] = self.process_user_query(''' Enter new hex color(skip this field for save old data)(type "default" for default color): ''', default_value = self.default_task["color"])

            storage.update_task(temp_task_group_id, temp_task_in_group_id, new_group_id = self.default_task["group_id"], new_text = self.default_task["text"], new_is_completed = self.default_task["is_completed"], new_color = self.default_task["color"])
        else: 
            groups = storage.get_all_groups()    

            self.default_group["id"] = self.process_user_query(" Enter group id: ", int) - 1

            self.default_group = {"id": groups[self.default_group["id"]]["id"], "text": groups[self.default_group["id"]]["text"], "color": groups[self.default_group["id"]]["color"]}

            self.default_group["text"] = self.process_user_query(" Enter new name(skip this field for save old data): ", default_value = self.default_group["text"])
            self.default_group["color"] = self.process_user_query(''' Enter new hex color(skip this field for save old data)(type "default" for default color): ''', default_value = self.default_group["color"])

            storage.update_group(self.default_group["id"], self.default_group["text"], self.default_group["color"])
            
update_task_or_group = QueryMethod()