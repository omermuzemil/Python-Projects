from turtle import *
from collections import Counter


def rectangle(horizontal, vertical, color):
    pendown()
    pensize(1)
    pencolor(color)
    begin_fill()
    for Counter in range(0, 2):
        forward(horizontal)
        right(90)
        forward(vertical)
        right(90)

    end_fill()
    penup()
    speed('slow')
    bgcolor('white')


# feet
fillcolor('purple')
penup()
goto(-100, -150)
pendown()
rectangle(50, 20, "purple")
goto(-30, -150)
rectangle(50, 20, 'purple')

# legs
fillcolor('grey')
goto(-25, -50)
rectangle(15, 100, 'grey')
goto(-55, -50)
rectangle(-15, 100, 'grey')

# body
fillcolor('red')
goto(-90, 100)
rectangle(100, 150, 'red')

# arms
fillcolor('grey')
goto(-150, 70)
rectangle(60, 15, 'grey')
goto(-150, 110)
rectangle(15, 40, 'grey')
goto(10, 70)
rectangle(60, 15, 'grey')
goto(55, 110)
rectangle(15, 40, 'grey')

# hands
fillcolor('green')
goto(-155, 130)
rectangle(25, 25, 'green')
goto(-147.5, 130)
fillcolor('white')
rectangle(10, 15, bgcolor())
fillcolor('green')
goto(50, 130)
rectangle(25, 25, 'green')
goto(58, 130)
fillcolor('white')
rectangle(10, 15, bgcolor())

# neck
fillcolor('grey')
goto(-50, 120)
rectangle(15, 20, 'grey')

# head
fillcolor('red')
goto(-85, 170)
rectangle(80, 50, 'red')

# eyes
fillcolor('white')
goto(-60, 160)
rectangle(30, 10, 'white')
goto(-55, 155)
fillcolor('black')
rectangle(5, 5, 'black')
goto(-40, 155)
rectangle(5, 5, 'black')

# mouth
goto(-65, 135)
right(0)
fillcolor('black')
rectangle(40, 5, 'black')
hideturtle()

mainloop()
