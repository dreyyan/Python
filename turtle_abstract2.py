import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
counter = 1
for _ in range(100):
    for _ in range(20):
        t.pencolor('red')
        t.forward(counter)
        t.left(160)
        counter += 1
    for _ in range(20):
        t.pencolor('orange')
        t.forward(counter)
        t.left(160)
        counter += 1
    for _ in range(20):
        t.pencolor('yellow')
        t.forward(counter)
        t.left(160)
        counter += 1
    for _ in range(20):
        t.pencolor('green')
        t.forward(counter)
        t.left(160)
        counter += 1
    for _ in range(20):
        t.pencolor('blue')
        t.forward(counter)
        t.left(160)
        counter += 1
    for _ in range(20):
        t.pencolor('violet')
        t.forward(counter)
        t.left(160)
        counter += 1
turtle.done()