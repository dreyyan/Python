import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
t.speed(0)
counter = 1
for _ in range(50):
    for _ in range(10):
        t.pencolor('orange')
        t.forward(counter)
        t.left(270)
        counter += 1
    for _ in range(10):
        t.pencolor('yellow')
        t.forward(counter)
        t.left(180)
        counter += 1
    for _ in range(10):
        t.pencolor('yellow')
        t.forward(counter)
        t.left(270)
        counter += 1
turtle.done()