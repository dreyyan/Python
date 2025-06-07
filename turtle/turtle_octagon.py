import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')
t.speed(100)
counter = 1
for _ in range(50):
    t.forward(counter)
    t.left(45)
    t.forward(counter * 2)
    counter += 1
turtle.done()