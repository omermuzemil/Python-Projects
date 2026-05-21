from turtle import *

pensize(2)
hideturtle()
goto(-140, 0)

def flag():
    for colors in  ["black", "red", "yellow"]:
        fillcolor(colors)
        begin_fill()
        for _ in range(2):
            forward(300)
            left(90)
            forward(50)
            left(90)
        end_fill()
        right(90)
        forward(50)
        left(90)
flag()


mainloop()