class Items:
    def __init__(self, array):
        self.array = array

    def __delitem__(self, index):
        print(f"Deleting Index {index}")
        del self.array[index]

    def __str__(self):
        return f"Array: {self.array}"

i1 = Items([1, 2, 3, 4, 5])
print(i1)
del i1[3]
print(i1)