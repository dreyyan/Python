def menuDecorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@menuDecorator
def greet(name) -> None:
    print(f"Hello, {name}!")

greet("Adrian")
