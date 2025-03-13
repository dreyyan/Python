def menu_decorator(displayMenu):
    def wrapper():
        print("MENU")
        print("-----------------------------")
        displayMenu()
        print("-----------------------------")
    return wrapper

@menu_decorator
def displayMenu():
    print("[1] | Create")
    print("[2] | Read")
    print("[3] | Update")
    print("[4] | Delete")

displayMenu()