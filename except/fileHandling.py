def readFile(filename) -> None:
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
    else:
        print(data)
        
readFile("dne.txt")
readFile("test.txt")
