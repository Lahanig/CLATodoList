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
                is_completed BOOLEAN
            )
        ''')

        self.close_db_connection_and_commit_changes()

    def get_all_groups(self):
        return [{"id": 0, "text": "Важно", "color": "#ff0000"}, {"id": 1, "text": "Менее важно", "color": "ffff00"}, {"id": 2, "text": "Не забыть", "color": "00ff00"}]

    def get_all_tasks(self):
        return [{"id": 0, "text": "Сделать рендер туду из бд aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "group_id": 0, "is_completed": False}, {"id": 1, "text": "Тыкать контент гач aaaaaaaaaaaaaaaa", "group_id": 1, "is_completed": False}, {"id": 2, "text": "Покакать", "group_id": 2, "is_completed": True}, {"id": 3, "text": "Сделать рендер туду из бд", "group_id": 2, "is_completed": False}]

storage_instance = Storage()