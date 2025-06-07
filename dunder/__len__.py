class Length:
    def __init__(self, array):
        self.array = array

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return f"Array: {self.array}"

l1 = Length([1, 2, 3])
print(l1)
print(len(l1))