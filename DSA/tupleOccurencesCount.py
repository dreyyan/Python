# PROBLEM: Given a tuple of values, count the # of occurences of a specified value
def tuple_occurences_count(tuple, element):
    count = 0 # To store the frequency of the element
    for i in tuple: # Iterate over elements in the tuple
        if i == elememt: # If value are the same
            count += 1 # Increment element frequency
    print(f"'{element}' occured {count} time/s")

tuple_test = (1, "Tree", 1, 65.3, False, "Word")
tuple_occurences_count(tuple_test, 1) # Test