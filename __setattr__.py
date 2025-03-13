class Attribute:
    def __init__(self):
        self.data = {}
    def __setattr__(self, item, attr):
        print("setting attribute...")
        self.__dict__[item] = attr

a1 = Attribute()
a1.attr = 3