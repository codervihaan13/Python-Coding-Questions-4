#18. Write a Python Turtle program to draw a rectangle using a loop.
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
width = 200
height = 100
for i in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
turtle.done()