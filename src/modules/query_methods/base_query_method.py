def query_method(func):
    def wrapper(*args, **kwargs):
        print(" ")
        result = func(*args, **kwargs)
        return result
    return wrapper

class BaseQueryMethod:
    default_group = {"id": 0, "text": "", "color": "default"}
    default_task = {"id": 0, "text": "", "group_id": 0, "in_group_id": 0, "is_completed": False, "color": "default"}

    def reset_default_values(self):
        self.default_group = {"id": 0, "text": "", "color": "default"}
        self.default_task = {"id": 0, "text": "", "group_id": 0, "in_group_id": 0, "is_completed": False, "color": "default"}

    def __init__(self):
        self.reset_default_values()

    def process_user_query(self, query_str, expected_output_type = str, default_value = None):
        result = input(query_str)

        if result == "":
            return default_value

        match expected_output_type.__name__:
            case 'str': 
                result = str(result)
            case 'int':
                result = int(result)
            case 'bool':
                match result:
                    case "y":
                        result = True
                    case "n":
                        result = False
                    case "1":
                        result = True
                    case "0":
                        result = False
                    case _:
                        result = False
        
        return result

    def render(self):
        pass

base_query_method = BaseQueryMethod()