from operator import getitem


class Items:
    def __init__(self, array):
        self.array = array

    def __getitem__(self, index):
        return self.array[index]

    def __str__(self):
        return f"Array: {self.array}"

i1 = Items([1, 2, 3, 4, 5])
print(i1)
print(getitem(i1, 2))