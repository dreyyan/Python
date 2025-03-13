print("List of Squares")

def list_of_squares(max_range):
    square_list = []
    for i in range(1, max_range + 1):
        square_list.append(i * i)
    print(square_list)

max_number = 20;
list_of_squares(max_number)