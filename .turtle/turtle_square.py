import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')
t.speed(100)
counter = 1
for _ in range(500):
    t.forward(counter)
    t.left(90)
    counter += 1
turtle.done()
