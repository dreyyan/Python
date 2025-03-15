import turtle
import math
turtle.bgcolor('black')
t = turtle.Turtle()
t.pencolor('white')
t.speed(100)
counter = 1
phi = (1 + math.sqrt(5)) / 2
for _ in range(200):
    t.forward(counter)
    t.left(20)
    counter = counter * phi * 0.67
turtle.done()