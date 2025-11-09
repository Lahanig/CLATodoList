def query_method(func):
    def wrapper(*args, **kwargs):
        print(" ")
        result = func(*args, **kwargs)
        return result
    return wrapper