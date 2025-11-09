from enum import Enum

class Query(Enum):
    LIST_ALL_TODO = 1
    CREATE_TODO = 2
    REMOVE_TODO = 3
    LIST_ALL_QUERY = 4
    CLEAR_ALL_TERMINAL = 5
    PRINT_WELCOME_SCREEN = 6
    EXIT = 7

if __name__ == '__module__':
    pass