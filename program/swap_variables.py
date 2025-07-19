def swap_variables(x, y):
    return y, x

x=1
y=2
x,y=swap_variables(x, y)
print(f'x = {x}\ny = {y}')