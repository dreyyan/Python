class Return:
    def __call__(self, num):
        return num + 5

r1 = Return()
print(r1(5))