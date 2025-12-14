from modules.query_methods.base_query_method import BaseQueryMethod, query_method
from modules.storage import storage_instance as storage

class QueryMethod(BaseQueryMethod):
    def __init__(self):
        super()

    @query_method
    def render(self):
        is_remove_task = True

        print("Remove task/group:")

        is_remove_task = self.process_user_query(" Remove task or group?(default: task)(y/n): ", bool, default_value = True)

        if is_remove_task == True:
            self.default_task["group_id"] = self.process_user_query(" Enter group id: ", int)
            self.default_task["in_group_id"] = self.process_user_query(" Enter task id in group: ", int)

            storage.remove_task(self.default_task["group_id"]-1, self.default_task["in_group_id"]-1)
        else: 
            self.default_group["id"] = self.process_user_query(" Enter group id: ", int)

            storage.remove_group(self.default_group["id"]-1)

remove_task_or_group = QueryMethod()