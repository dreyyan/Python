class lessThan5:
    def __init__ (self, num):
        self.num = num
    def __iter__(self):
        self.current = self.num
        return self
    def __next__(self):
        if self.current < 5:
            raise StopIteration
        self.current -= 1
        return self.current
        
numbers = lessThan5(10)
        
for i in numbers:
    print(i) 
                    