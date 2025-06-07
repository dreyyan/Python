class Compare:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __lt__(self, other):
        print("compare if less than...")
        return self.num1 < self.num2
    def __gt__(self, other):
        print("compare if greater than...")
        return self.num1 > self.num2
    def __repr__(self):
        return f"Compare: {self.num1} < {self.num2}"        
      
n1 = Compare(5, 10)
n2 = Compare(10, 5)
print(n1 > n2)
print(n1 < n2)