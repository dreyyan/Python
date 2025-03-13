class Name:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Name({self.name})"
        
n1 = Name("Adrian")
print(repr(n1))      