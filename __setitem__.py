class Items:
    def __init__(self, array):
        self.array = array

    def __setitem__(self, index, value):
        print(f"Set Index {index} to {value}")
        self.array[index] = value

    def __str__(self):
        return f"Array: {self.array}"

i1 = Items([1, 2, 3, 4, 5])
print(i1)
i1[3] = 50
print(i1)