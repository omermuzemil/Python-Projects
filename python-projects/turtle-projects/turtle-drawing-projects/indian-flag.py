from turtle import *
hideturtle()
speed(0)
pensize(2)
goto(-130, 0)


# flag
def flag():
    for colors in ["orange", "white", "green"]:
        fillcolor(colors)
        begin_fill()
        for i in range(2):
            forward(300)
            left(90)
            forward(70)
            left(90)
        end_fill()
        right(90)
        forward(70)
        left(90)
# circle
    pensize(4)
    pencolor("blue")
    penup()
    goto(30, -65)
    pendown()
    circle(30)

# small circle
    pensize(2)
    pencolor("blue")
    fillcolor("blue")
    begin_fill()
    penup()
    goto(30, -43)
    pendown()
    circle(6)
    end_fill()


flag()

# line


def line():
    pencolor("blue")
    penup()
    goto(30, -37)
    pendown()
    right(90)
    forward(23)


for i in range(16):
    line()
    left(5)
line()

mainloop()
