from modules.query_methods.query_method_decorator import query_method
from modules.storage import storage_instance as storage

@query_method
def create_new_task_or_group():
    temp_group = {"id": 0, "text": "", "color": "default"}
    temp_task = {"id": 0, "text": "", "group_id": 0, "in_group_id": 0, "is_completed": False, "color": "default"}
    is_create_new_group = False

    print("Create new task/group:")

    temp_flag = input(" Create new task or group?(default: task)(y/n): ") or "y"

    if temp_flag.lower() != "y":
        is_create_new_group = True
    else: is_create_new_group = False

    if is_create_new_group == True:
        temp_group["text"] = input(" Enter name: ")
        temp_group["color"] = input(" Enter hex color(skip this field for default color): ") or temp_group["color"]

        temp_group["id"] = len(storage.get_all_groups())

        storage.create_new_group(temp_group["id"], temp_group["text"], temp_group["color"])
    else: 
        temp_task["text"] = input(" Enter text: ")
        temp_task["group_id"] = int(input(" Enter group id: ")) or 0
        temp_task["color"] = input(" Enter hex color(skip this field for default color): ") or temp_task["color"]

        temp_tasks = storage.get_all_tasks()

        temp_task["id"] = len(temp_tasks)

        i = 0
        for task in temp_tasks:
            if task["group_id"] == temp_task["group_id"]-1:
                i = task["in_group_id"]+1
        
        temp_task["in_group_id"] = i

        storage.create_new_task(temp_task["id"], temp_task["text"], temp_task["group_id"]-1, temp_task["in_group_id"], temp_task["is_completed"], temp_task["color"])