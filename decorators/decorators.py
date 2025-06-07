def menuDecorator(func) -> None:
    def wrapper():
        func()
        print(", user!")
    return wrapper


@menuDecorator
def greet() -> None:
    print("hello", end='')

greet()
