import turtle

s1 = turtle.Screen()
s1.bgcolor("white")
pen = turtle.Turtle()
pen.speed(2)
pen.width(3)
pen.color("red", "pink")   
pen.begin_fill()
pen.left(140)
pen.forward(180)

pen.circle(-90, 200)
pen.left(120)

pen.circle(-90, 200)
pen.forward(180)

pen.end_fill()

pen.hideturtle()

turtle.done()
