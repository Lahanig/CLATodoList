from enum import Enum

class Query(Enum):
    NONE = 0
    LIST_ALL_TODO = 1
    CREATE_TODO_OR_GROUP = 2
    UPDATE_TODO_OR_GROUP = 3
    REMOVE_TODO_OR_GROUP = 4
    LIST_ALL_QUERY = 5
    CLEAR_ALL_TERMINAL = 6
    PRINT_WELCOME_SCREEN = 7
    EXIT = 8

if __name__ == '__module__':
    pass