class Operations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.symbol = ''

    def __add__(self, other):
        print("adding numbers...")
        symbol = '+'
        return self.num1 + self.num2

    def __sub__(self, other):
        print("subtracting numbers...")
        symbol = '-'
        return self.num1 - self.num2

    def __mul__(self, other):
        print("multiplying numbers...")
        symbol = 'x'
        return self.num1 * self.num2

    def __repr__(self):
        return f"Operation: {self.num1} {symbol} {self.num2}"


n1 = Operations(5, 10)
n2 = Operations(10, 5)
result = n1 + n2
print(repr(result))
result = n1 - n2
print(repr(result))
result = n1 * n2
print(repr(result))