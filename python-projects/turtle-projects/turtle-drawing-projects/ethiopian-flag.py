from turtle import *

pensize(2)
hideturtle()
goto(-120, 0)

# Green
color("green")
begin_fill()
for i in range(2):
    forward(300)
    left(90)
    forward(50)
    left(90)
end_fill()
right(90)

# yellow
color("yellow")
begin_fill()
forward(50)
left(90)
for i in range(2):
    forward(300)
    left(90)
    forward(50)
    left(90)
end_fill()
right(90)

# Red
color("red")
begin_fill()
forward(50)
left(90)
for i in range(2):
    forward(300)
    left(90)
    forward(50)
    left(90)
end_fill()

penup()
goto(35, -48)
pendown()

# Circle
color("blue")
begin_fill()
circle(25)
end_fill()

penup()
goto(10, -18)
pendown()

# Star
color("yellow")
for i in range(5):
    forward(50)
    right(144)

mainloop()
