import turtle
pen=turtle.Turtle()
s1=turtle.Screen()
pen.speed(10)
pen.color("red","yellow")
pen.begin_fill()
while True:
    pen.fd(300)
    pen.lt(170)
    if pen.heading()==0:
        break
pen.end_fill()
s1.exitonclick()
