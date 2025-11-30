import sqlite3

class Storage:
    conn = None
    cursor = None

    def create_db_connection(self):
        self.conn = sqlite3.connect('./modules/db/storage.db')
        self.cursor = self.conn.cursor()

    def close_db_connection_and_commit_changes(self):
        self.conn.commit()
        self.conn.close()

    def __init__(self):
        self.create_db_connection()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY,
                text TEXT,
                color TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                text TEXT,
                group_id INTEGER,
                is_completed BOOLEAN,
                color TEXT
            )
        ''')

        self.close_db_connection_and_commit_changes()

    def get_all_groups(self):
        self.create_db_connection()
        self.cursor.execute("SELECT * FROM groups")

        rows = self.cursor.fetchall()
        self.close_db_connection_and_commit_changes()

        temp_groups = []

        for group in rows:
            temp_groups.append({"id": group[0], "text": group[1], "color": group[2]})

        return temp_groups

    def get_all_tasks(self):
        self.create_db_connection()
        self.cursor.execute("SELECT * FROM tasks")

        rows = self.cursor.fetchall()
        self.close_db_connection_and_commit_changes()

        temp_tasks = []

        for task in rows:
            temp_tasks.append({"id": task[0], "text": task[1], "group_id": task[2], "is_completed": task[3], "color": task[4]})

        return temp_tasks

    def create_new_group(self, new_id, new_text, new_color):
        self.create_db_connection()
        self.cursor.execute("INSERT INTO groups (id, text, color) VALUES (?, ?, ?)", (new_id, new_text, new_color))
        self.close_db_connection_and_commit_changes()

    def create_new_task(self, new_id, new_text, new_group_id, new_is_completed, new_color):
        self.create_db_connection()
        self.cursor.execute("INSERT INTO tasks (id, text, group_id, is_completed, color) VALUES (?, ?, ?, ?, ?)", (new_id, new_text, new_group_id, new_is_completed, new_color))
        self.close_db_connection_and_commit_changes()

    def create_default_groups(self):
        temp_groups = [{"id": 0, "text": "Важно", "color": "#ff0000"}, {"id": 1, "text": "Менее важно", "color": "ffff00"}, {"id": 2, "text": "Не забыть", "color": "00ff00"}]

        for temp_group in temp_groups:
            self.create_new_group(temp_group["id"], temp_group["text"], temp_group["color"])

    def create_default_tasks(self):
        temp_tasks = [{"id": 0, "text": "Сделать рендер туду из бд aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "group_id": 0, "is_completed": False, "color": "default"}, {"id": 1, "text": "Тыкать контент гач aaaaaaaaaaaaaaaa", "group_id": 1, "is_completed": False, "color": "ff0000"}, {"id": 2, "text": "Покакать", "group_id": 2, "is_completed": True, "color": "ffff00"}, {"id": 3, "text": "Сделать рендер туду из бд", "group_id": 2, "is_completed": False, "color": "00ff10"}]

        for temp_task in temp_tasks:
            self.create_new_task(temp_task["id"], temp_task["text"], temp_task["group_id"], temp_task["is_completed"], temp_task["color"])

storage_instance = Storage()