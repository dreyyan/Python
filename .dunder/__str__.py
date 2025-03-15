class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Welcome, {self.name}"
        
n1 = Name("Adrian")
print(str(n1))        