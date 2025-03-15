def fruit_has_letter(array, letter):
    tuple = set()
    counter = 0

    for element in array:
        array[counter] = element.lower()
        counter += 1

    for i in array:
        for char in i:
            if char == letter:
                tuple.add(i)

    print(tuple)
fruit_list = ["Grape", "Lemon", "Apple", "Pear"]
fruit_has_letter(fruit_list, 'a')