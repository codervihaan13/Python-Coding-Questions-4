#19. Write a Python Turtle program to draw an equilateral triangle and a regular pentagon using loops.
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(-150, -50)
t.pendown()
side_length = 100
for i in range(3):
    t.forward(side_length)
    t.left(120)
t.penup()
t.goto(50, -50)
t.pendown()
for j in range(5):
    t.forward(side_length)
    t.left(72)
turtle.done()