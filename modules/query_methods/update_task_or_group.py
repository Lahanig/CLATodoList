from modules.query_methods.query_method_decorator import query_method
from modules.storage import storage_instance as storage

@query_method
def update_task_or_group():
    temp_group = {"id": 0, "text": "", "color": "default"}
    temp_task = {"id": 0, "text": "", "group_id": 0, "in_group_id": 0, "is_completed": False, "color": "default"}
    is_update_group = False

    print("Update data in task/group:")

    temp_flag = input(" Update task or group?(default: task)(y/n): ") or "y"

    if temp_flag.lower() != "y":
        is_update_group = True
    else: is_update_group = False

    if is_update_group == True:
        groups = storage.get_all_groups()    

        temp_group["id"] = int(input(" Enter group id: ")) - 1

        temp_group = {"id": groups[temp_group["id"]]["id"], "text": groups[temp_group["id"]]["text"], "color": groups[temp_group["id"]]["color"]}

        temp_group["text"] = input(" Enter new name(skip this field for save old data): ") or temp_group["text"]
        temp_group["color"] = input(''' Enter new hex color(skip this field for save old data)(type "default" for default color): ''') or temp_group["color"]

        storage.update_group(temp_group["id"], temp_group["text"], temp_group["color"])
    else: 
        tasks = storage.get_all_tasks()
        
        temp_task_group_id = int(input(" Enter task group id: "))-1
        temp_task_in_group_id = int(input(" Enter task id in group: "))-1

        for task in tasks:
            if task["group_id"] == temp_task_group_id and task["in_group_id"] == temp_task_in_group_id:
                temp_task = {"id": task["id"], "text": task["text"], "group_id": task["group_id"], "in_group_id": task["in_group_id"], "is_completed": task["is_completed"], "color": task["color"]}

        temp_task["text"] = input(" Enter new name(skip this field for save old data): ") or temp_task["text"]
        temp_task["group_id"] = int(input(" Enter task new group id(skip this field for save old data): ") or temp_task["group_id"] + 1) - 1 
        # temp_task["in_group_id"] = int(input(" Enter new task id in group(skip this field for save old data): ")) or temp_task["in_group_id"]
        temp_task_is_completed = input(" Complete task?(y/n)(default: n): ").lower or "n"

        if temp_task_is_completed == "y":
            temp_task["is_completed"] = True
        else: temp_task["is_completed"] = False

        temp_task["color"] = input(''' Enter new hex color(skip this field for save old data)(type "default" for default color): ''') or temp_task["color"]

        storage.update_task(temp_task_group_id, temp_task_in_group_id, new_group_id = temp_task["group_id"], new_text = temp_task["text"], new_is_completed = temp_task["is_completed"], new_color = temp_task["color"])