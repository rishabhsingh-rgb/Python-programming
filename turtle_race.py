import turtle
import random

def no_of_turtles():
    while True:
        count=input("Enter the number of turtles you want to race(2 to 10): ")
        if count.isdigit():
            count=int(count)
        else:
            print("Plz enter numeric value between 2 to 10.")    
            continue
        if 2<=count<=10:
            return count
        else:
            print("Input out of range, try again.....")


color_list=["green","yellow","red","blue","orange","pink","brown","grey","aquamarine1","white"]
random.shuffle(color_list)            
t=no_of_turtles()        
s1=turtle.Screen()
s1.bgcolor("black")
s1.setup(width=600,height=500)
width=600
height=500
turtle_list=[]
gap=width//(t+1)
for i in range(1,t+1):
    new=turtle.Turtle()
    new.color(color_list[i-1])
    new.shape("turtle")
    new.lt(90)
    new.penup()
    new.goto((-width//2 + (i*gap)),-height//2+20)
    turtle_list.append(new)

def race():
    race_on=True
    while race_on:
        for turtles in turtle_list:
            distance=random.randint(1,10)
            turtles.forward(distance)
            x,y=turtles.pos()
            if y>=height//2-15:
                print(f"The winner is {turtles.pencolor()} colored turtle.")
                race_on=False

race()
s1.exitonclick()    
