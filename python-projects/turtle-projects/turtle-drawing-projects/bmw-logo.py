from turtle import *
hideturtle()
speed(0)
pensize(7)
pencolor("#c7d9e2")

# black circle
fillcolor("black")
begin_fill()
penup()
goto(0, -100)
pendown()
circle(150)
end_fill()

# blue 1/4 circle
fillcolor("#5eb2d8")
begin_fill()
penup()
goto(0, -50)
pendown()
circle(100)
end_fill()

# white 1/4 circle 1
pensize(1)
fillcolor("white")
begin_fill()
goto(0, 50)
back(100)
right(90)
circle(100, 90)
end_fill()

# white 1/4 circle 2
goto(0, 50)
begin_fill()
left(90)
forward(100)
goto(100, 50)
end_fill()
begin_fill()
circle(100, 90)
end_fill()

# b
penup()
goto(-125, 80)
pendown()
pencolor("white")
write('B', font=("arial", 35, "bold"))

# M
penup()
goto(-20, 145)
pendown()
pencolor("white")
write('M', font=("arial", 35, "bold"))

# w
penup()
goto(90, 80)
pendown()
pencolor("white")
write('W', font=("arial", 35, "bold"))

mainloop()
