import time
import turtle
from turtle import Turtle
from random import randint

#Window Setup
window = turtle.Screen()
window.title("TURTLE RACE")
turtle.bgcolor("lightgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200) #set position
turtle.write("TURTLE RACE", font=("Arial", 30, "bold"))
turtle.penup()

#dirt on the bottom of the page
turtle.setpos(-400, -180)
turtle.color("sandybrown")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#Finish Line
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()


#turtle 1

turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("red")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()


#turtle 2

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("blue")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

#turtle 3

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("yellow")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

#turtle 4

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("magenta")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

#pause the game before it begins

time.sleep(1)

#move the turte forward

for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))

turtle.exitonclick()

#add winner to the race





