from modules.query_methods.query_method_decorator import query_method
from modules.storage import storage_instance as storage

@query_method
def remove_task_or_group():
    temp_group = { "id": 0 }
    temp_task = { "group_id": 0, "in_group_id": 0 }
    is_remove_group = False

    print("Remove task/group:")

    temp_flag = input(" Remove task or group?(default: task)(y/n): ") or "y"

    if temp_flag.lower() != "y":
        is_remove_group = True
    else: is_remove_group = False

    if is_remove_group == True:
        temp_group["id"] = int(input(" Enter group id: "))
        storage.remove_group(temp_group["id"]-1)
    else: 
        temp_task["group_id"] = int(input(" Enter group id: "))
        temp_task["in_group_id"] = int(input(" Enter task id in group: "))
        storage.remove_task(temp_task["group_id"]-1, temp_task["in_group_id"]-1)