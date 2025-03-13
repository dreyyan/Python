class Attribute:
    def __getattr__(self, item):
        return f"{item} does not exist"

a1 = Attribute()
print(a1.someattr)