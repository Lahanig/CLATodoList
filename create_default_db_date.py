from modules.storage import storage_instance as storage

def main():
    storage.create_default_groups()
    storage.create_default_tasks()

if __name__ == "__main__":
    main()