import sys

from modules.types.query import Query
from modules.query_methods.list_all_todo import render
from modules.query_methods.list_all_query import list_all_query
from modules.query_methods.print_welcome_screen import print_welcome_screen
from modules.query_methods.create_new_task_or_group import create_new_task_or_group
from modules.query_methods.update_task_or_group import update_task_or_group
from modules.query_methods.remove_task_or_group import remove_task_or_group
from modules.utility import utility_instance as utility

class UI:
    current_query = Query.PRINT_WELCOME_SCREEN

    def __init__(self):
        pass

    def invoke_query_method(self):
        match self.current_query:
            case Query.NONE:
                pass
            case Query.LIST_ALL_QUERY:
                list_all_query()
            case Query.LIST_ALL_TODO:
                render.list_all_todo()
            case Query.CLEAR_ALL_TERMINAL:
                utility.clear_screen()
            case Query.PRINT_WELCOME_SCREEN:
                print_welcome_screen()
            case Query.CREATE_TODO_OR_GROUP:
                create_new_task_or_group()
            case Query.UPDATE_TODO_OR_GROUP:
                update_task_or_group()
            case Query.REMOVE_TODO_OR_GROUP:
                remove_task_or_group()
            case Query.EXIT:
                sys.exit(0)

    def query(self):
        temp_query = input("\n$ ").lower()

        match temp_query:
            case "help":
                self.current_query = Query.LIST_ALL_QUERY
            case "ls":
                self.current_query = Query.LIST_ALL_TODO
            case "clear":
                self.current_query = Query.CLEAR_ALL_TERMINAL
            case "welcome":
                self.current_query = Query.PRINT_WELCOME_SCREEN
            case "create":
                self.current_query = Query.CREATE_TODO_OR_GROUP
            case "update":
                self.current_query = Query.UPDATE_TODO_OR_GROUP
            case "remove":
                self.current_query = Query.REMOVE_TODO_OR_GROUP
            case "exit":
                self.current_query = Query.EXIT
            case _:
                self.current_query = Query.NONE 
                
UI_instance = UI()  