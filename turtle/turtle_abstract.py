import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
t.speed(100)
counter = 1
for _ in range(100):
    for _ in range(20):
        if counter % 2 == 0:
            t.penup()
        else:
            t.pendown()
        t.pencolor('white')
        t.forward(counter)
        t.left(70)
        counter += 1
    for _ in range(20):
        if counter % 2 == 0:
            t.penup()
        else:
            t.pendown()
        t.pencolor('red')
        t.forward(counter)
        t.left(70)
        counter += 1
turtle.done()