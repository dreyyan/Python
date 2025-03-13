class Compare:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __eq__(self, other):
        print("compare if equal to...")
        return self.num1 == self.num2

    def __ne__(self, other):
        print("compare if not equal to...")
        return self.num1 != self.num2

    def __str__(self):
        return f"{self.num1} = / != {self.num2}"


n1 = Compare(5, 10)
n2 = Compare(10, 5)
print(n1)
print(n1 == n2)
print(n1 != n2)