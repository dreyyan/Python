class Operations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.symbol = ''

    def __truediv__(self, other):
        print("true division...")
        symbol = '/'
        return self.num1 / self.num2

    def __floordiv__(self, other):
        print("floor division...")
        symbol = '/'
        return self.num1 // self.num2

    def __str__(self):
        return f"{self.num1} {symbol} {self.num2}"


n1 = Operations(10, 5)
n2 = Operations(20, 5)
result = n1 / n2
print(str(result))
result = n1 // n2
print(str(result))