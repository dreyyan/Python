def readFile(filename) -> None:
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
    else:
        print(f"[ FILE DETAILS ]")
        print(f"Name: {file.name}")
        print(f"Mode: {file.mode}")
        print(data, end='')
    finally:
        print("* process finished")

readFile("code/Python/file/test.txt")

# Operations
# .read()       | read whole content
# .readline()   | read one line
# .readlines()  | read lines as list
# .name, .mode, .closed
