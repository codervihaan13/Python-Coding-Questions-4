#20. Write a Python Turtle program to draw a flower using six circles arranged in a circular pattern
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
radius = 60
for i in range(6):
    t.circle(radius)
    t.left(60)
t.dot(20)
turtle.done()