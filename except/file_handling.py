def read_file(filename) -> None:
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
    else:
        print(data)
        
read_file("dne.txt")
read_file("test.txt")
