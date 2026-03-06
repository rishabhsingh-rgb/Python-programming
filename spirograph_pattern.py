import turtle
import random
turtle.colormode(255)
s1=turtle.Screen()
pen=turtle.Turtle()
pen.speed(0)
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    pen.color((r,g,b))
    pen.circle(100)
    pen.lt(5)
    if pen.heading()==0:
        break

s1.exitonclick()
