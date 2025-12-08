import sqlite3
import os
from pathlib import Path

class Storage:
    conn = None
    cursor = None
    is_dev_mode = False

    def create_db_connection(self):
        temp_storage_path = "./modules/db"
        
        if self.is_dev_mode == False:
            temp_path = Path.home()

            temp_storage_path = f"{temp_path}/CLATodoList/db"

        if not os.path.exists(temp_storage_path):
            os.makedirs(temp_storage_path)

        self.conn = sqlite3.connect(temp_storage_path + '/storage.db')
        self.cursor = self.conn.cursor()

    def close_db_connection_and_commit_changes(self):
        self.conn.commit()
        self.conn.close()

    def init_db(self):
        self.create_db_connection()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER,
                text TEXT,
                color TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER,
                text TEXT,
                group_id INTEGER,
                in_group_id INTEGER,
                is_completed BOOLEAN,
                color TEXT
            )
        ''')

        self.close_db_connection_and_commit_changes()

    def __init__(self):
        self.init_db()
    
    def update_groups_table_ids(self):
        self.create_db_connection()

        self.cursor.execute("SELECT rowid, * FROM groups")
        rows = self.cursor.fetchall()

        i = 0
        for group in rows:
            self.cursor.execute("UPDATE groups SET id = ?, text = ?, color = ? WHERE rowid = ?", (i, group[2], group[3], group[0]))
            i += 1

        self.close_db_connection_and_commit_changes()

    def update_tasks_table_ids(self):
        self.create_db_connection()

        self.cursor.execute("SELECT rowid, * FROM tasks")
        rows = self.cursor.fetchall()

        i = 0
        for task in rows:
            self.cursor.execute("UPDATE tasks SET id = ?, text = ?, group_id = ?, in_group_id = ?, is_completed = ?, color = ? WHERE rowid = ?", (i, task[2], task[3], task[4], task[5], task[6], task[0]))
            i += 1

        self.close_db_connection_and_commit_changes()

    def get_all_groups(self):
        self.init_db()
        self.create_db_connection()
        self.cursor.execute("SELECT * FROM groups")

        rows = self.cursor.fetchall()
        self.close_db_connection_and_commit_changes()

        temp_groups = []

        for group in rows:
            temp_groups.append({"id": group[0], "text": group[1], "color": group[2]})

        return temp_groups

    def get_all_tasks(self):
        self.init_db()
        self.create_db_connection()
        self.cursor.execute("SELECT * FROM tasks")

        rows = self.cursor.fetchall()
        self.close_db_connection_and_commit_changes()

        temp_tasks = []

        for task in rows:
            temp_tasks.append({"id": task[0], "text": task[1], "group_id": task[2], "in_group_id": task[3], "is_completed": task[4], "color": task[5]})

        return temp_tasks

    def create_new_group(self, new_id, new_text, new_color):
        self.init_db()
        self.create_db_connection()

        self.cursor.execute("INSERT INTO groups (id, text, color) VALUES (?, ?, ?)", (new_id, new_text, new_color))
        self.close_db_connection_and_commit_changes()

    def create_new_task(self, new_id, new_text, new_group_id, new_in_group_id, new_is_completed, new_color):
        self.init_db()
        self.create_db_connection()
        self.cursor.execute("INSERT INTO tasks (id, text, group_id, in_group_id, is_completed, color) VALUES (?, ?, ?, ?, ?, ?)", (new_id, new_text, new_group_id, new_in_group_id, new_is_completed, new_color))
        self.close_db_connection_and_commit_changes()

    def update_group(self, group_id, new_text = None, new_color = None):
        self.init_db()
        self.create_db_connection()

        if new_text != None:
            self.cursor.execute("UPDATE groups SET text = ? WHERE id = ?", (new_text, group_id))
        if new_color != None:
            self.cursor.execute("UPDATE groups SET color = ? WHERE id = ?", (new_color, group_id))

        self.close_db_connection_and_commit_changes()

    def update_task(self, task_id, new_text = None, new_group_id = None, new_in_group_id = None, new_is_completed = None, new_color = None):
        self.init_db()
        self.create_db_connection()

        if new_text != None:
            self.cursor.execute("UPDATE tasks SET text = ? WHERE id = ?", (new_text, task_id))
        if new_group_id != None:
            self.cursor.execute("UPDATE tasks SET group_id = ? WHERE id = ?", (new_group_id, task_id))
        if new_in_group_id != None:
            self.cursor.execute("UPDATE tasks SET in_group_id = ? WHERE id = ?", (new_in_group_id, task_id))
        if new_is_completed != None:
            self.cursor.execute("UPDATE tasks SET is_completed = ? WHERE id = ?", (new_is_completed, task_id))    
        if new_color != None:
            self.cursor.execute("UPDATE tasks SET color = ? WHERE id = ?", (new_color, task_id))

        self.close_db_connection_and_commit_changes()

    def remove_group(self, group_id):
        self.init_db()
        self.create_db_connection()
        self.cursor.execute("DELETE FROM groups WHERE id = ?", (str(group_id)))
        self.close_db_connection_and_commit_changes()

        self.update_groups_table_ids()

    def remove_task(self, new_group_id, new_in_group_id):
        self.init_db()
        self.create_db_connection()
        self.cursor.execute("DELETE FROM tasks WHERE group_id = ? and in_group_id = ?", (str(new_group_id), str(new_in_group_id)))
        self.close_db_connection_and_commit_changes()

        self.update_tasks_table_ids()

        self.create_db_connection()

        self.cursor.execute("SELECT rowid, * FROM tasks WHERE group_id = ?", (str(new_group_id)))
        rows = self.cursor.fetchall()

        i = 0
        for task in rows:
            self.cursor.execute("UPDATE tasks SET id = ?, text = ?, group_id = ?, in_group_id = ?, is_completed = ?, color = ? WHERE rowid = ?", (task[1], task[2], task[3], i, task[5], task[6], task[0]))
            i += 1

        self.close_db_connection_and_commit_changes()

    def create_default_groups(self):
        temp_groups = [{"id": 0, "text": "Важно", "color": "#ff0000"}, {"id": 1, "text": "Менее важно", "color": "ffff00"}, {"id": 2, "text": "Не забыть", "color": "00ff00"}]

        for temp_group in temp_groups:
            self.create_new_group(temp_group["id"], temp_group["text"], temp_group["color"])

    def create_default_tasks(self):
        temp_tasks = [{"id": 0, "text": "Сделать рендер туду из бд aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "group_id": 0, "in_group_id": 0, "is_completed": False, "color": "default"}, {"id": 1, "text": "Тыкать контент гач aaaaaaaaaaaaaaaa", "group_id": 1, "in_group_id": 0, "is_completed": False, "color": "ff0000"}, {"id": 2, "text": "Покакать", "group_id": 2, "in_group_id": 0, "is_completed": True, "color": "ffff00"}, {"id": 3, "text": "Сделать рендер туду из бд", "group_id": 2, "in_group_id": 1, "is_completed": False, "color": "00ff10"}]

        for temp_task in temp_tasks:
            self.create_new_task(temp_task["id"], temp_task["text"], temp_task["group_id"], temp_task["in_group_id"], temp_task["is_completed"], temp_task["color"])

storage_instance = Storage()