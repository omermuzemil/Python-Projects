from turtle import *
hideturtle()
speed(0)
pensize(2)
bgcolor("black")

for i in range(360):
    colors = ["green", "yellow", "red", "blue", "purple", "orange"]
    color(colors[i % 6])
    forward(i)
    left(299)

mainloop()
