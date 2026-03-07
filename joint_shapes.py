import turtle
import random
s1=turtle.Screen()
pen=turtle.Turtle()
pen.speed(2)
pen.pensize(3)
colors=["red","black","pink","yellow","blue","grey","orange","brown","aquamarine"]
for i in range(3,10):
    angle=360/i
    pen.color(random.choice(colors))
    for j in range(i):
        pen.fd(100)
        pen.lt(angle)
s1.exitonclick() 
