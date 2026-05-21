from turtle import *

pensize(3)
bgcolor('black')
speed(0)

def triangle():
    for _ in range(3):
        for colors in ['red', 'yellow', 'blue']:
            color(colors)
            forward(150)
            left(120)
            forward(150)
            left(120)
            forward(150)

for _ in range(15):
    triangle()
    left(5)
hideturtle()


mainloop()