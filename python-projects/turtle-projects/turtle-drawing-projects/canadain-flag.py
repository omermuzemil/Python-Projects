from turtle import *
hideturtle()
speed(0)
pensize(2)
goto(-150, -100)

# red flag

fillcolor("red")
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(200)
    left(90)
end_fill()
forward(100)

# white flag

fillcolor("white")
begin_fill()
for i in range(2):
    forward(130)
    left(90)
    forward(200)
    left(90)
end_fill()
forward(130)

# red flag 2

fillcolor("red")
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(200)
    left(90)
end_fill()
forward(100)

# leaf
pencolor("red")
penup()
goto(7, -70)
pendown()
fillcolor("red")
begin_fill()

forward(10)
left(100)
forward(30)

right(105)
forward(37)
left(120)
forward(15)

right(80)
forward(40)
left(120)
forward(15)
right(90)
forward(20)

left(144)
forward(20)
right(100)
forward(15)
left(120)
forward(20)

right(140)
forward(40)
left(130)
forward(12)
right(100)
forward(25)

left(130)
forward(25)
right(120)
forward(12)
left(140)
forward(40)

right(130)
forward(20)
left(110)
forward(15)
right(90)
forward(20)

left(140)
forward(20)
right(90)
forward(15)
left(120)
forward(40)

right(105)
forward(20)
left(145)
forward(37)
right(110)
forward(30)

end_fill()

mainloop()
