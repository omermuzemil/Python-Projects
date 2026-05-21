# Simple snake game in python3
# Instructinos:
#     W = go up
#     S = go down
#     D = go right
#     A = go_left
#     Everytime the snake eats the apple the speed of the snake increases by 0.001.


import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @CodingWithPython")
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food(Apple)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center",
          font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Keyboadrd bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1200, 1200)

        # Clear the segments list
        segments.clear()

        # Reset the score after collision with border
        score = 0

        # reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(
            score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision between food
    if head.distance(food) < 20:
        # Move the food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segments
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("grey")
        new_tail.penup()
        segments.append(new_tail)

        # shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(
            score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the last segments toward fore-list, in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segment
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1200, 1200)

            # Clear the segments list
            segments.clear()

            # Reset the score after collision with body segmeent
            score = 0

            # reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(
                score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
