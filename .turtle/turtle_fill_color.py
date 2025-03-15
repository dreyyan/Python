import turtle

turtle.bgcolor('black')
t = turtle.Turtle()
t.fillcolor("white")
t.begin_fill()
t.pencolor("white")
t.speed(5)
for _ in range(4):
    t.forward(100)
    t.left(90)
t.right(90)
for _ in range(4):
    t.forward(100)
    t.left(90)
t.right(90)
for _ in range(4):
    t.forward(100)
    t.left(90)
t.right(90)
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
turtle.done()