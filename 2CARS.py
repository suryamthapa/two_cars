#to make the two cars game

import turtle
import time
import random

score = 0
highscore = 0
delay = 0.1

# screen
wn = turtle.Screen()
wn.title("two cars with me")
wn.bgcolor("grey")
wn.setup(height=600, width=600)
wn.tracer(0)

def cursors():
    # cursor
    cone = turtle.Turtle()
    cone.color("white")
    cone.speed(0)
    cone.penup()
    cone.goto(-290, -290)
    cone.pendown()
    cone.goto(-290, 290)

    ctwo = turtle.Turtle()
    ctwo.color("white")
    ctwo.speed(0)
    ctwo.penup()
    ctwo.goto(-145, -290)
    ctwo.pendown()
    ctwo.goto(-145, 290)

    cthree = turtle.Turtle()
    cthree.color("blue")
    cthree.speed(0)
    cthree.penup()
    cthree.goto(0, -290)
    cthree.pendown()
    cthree.goto(0, 290)

    cfour = turtle.Turtle()
    cfour.color("white")
    cfour.speed(0)
    cfour.penup()
    cfour.goto(145, -290)
    cfour.pendown()
    cfour.goto(145, 290)

    cfive = turtle.Turtle()
    cfive.color("white")
    cfive.speed(0)
    cfive.penup()
    cfive.goto(290, -290)
    cfive.pendown()
    cfive.goto(290, 290)


cursors()
# cars
carone = turtle.Turtle()
carone.color("red")
carone.shape("square")
carone.speed(0)
carone.resizemode("user")
carone.shapesize(1, 1)
carone.penup()
carone.goto(-217.5, -250)
carone.direction = "stop"

cartwo = turtle.Turtle()
cartwo.color("green")
cartwo.shape("square")
cartwo.resizemode("user")
cartwo.shapesize(1, 1)
cartwo.speed(0)
cartwo.penup()
cartwo.goto(217.5, -250)
cartwo.direction = "stop"

# scoreboard
board = turtle.Turtle()
board.shape("square")
board.color("white")
board.penup()
board.goto(175, 230)
board.hideturtle()
board.write(f" Score : {score} \n Highscore : {highscore}", align="center", font=("Courier", 16, "normal"))


# start the game
star = turtle.Turtle()
star.color("white")
star.shape("square")
star.penup()
star.hideturtle()
star.write("Press S to Start", align="center", font=("Courier", 30, "normal"))

# turtle to show that the game is paused
paus = turtle.Turtle()
paus.color("white")
paus.shape("square")
paus.penup()
paus.hideturtle()
paus.write("")

new = turtle.Turtle()
new.color("white")
new.shape("square")
new.hideturtle()


command = "stop"
things = []
circles = []
obstacles = []
n = 0 # to create the turtles after game over


# obstacles and circles
def f_create():
    a1 = random.choice(["right", "left"])
    b1 = random.choice(["circle", "obstacle"])
# to create the obstacles and circles in the right side
    if b1 == "circle" and a1 == "right":
        circle = turtle.Turtle()
        circle.shape("circle")
        circle.color("magenta")
        circle.penup()
        circle.goto(217.5, 290)
        things.append(circle)
        circles.append(circle)
    elif b1 == "circle" and a1 == "left":
        circle = turtle.Turtle()
        circle.shape("circle")
        circle.color("magenta")
        circle.penup()
        circle.goto(72.5, 290)
        things.append(circle)
        circles.append(circle)
    elif b1 == "obstacle" and a1 == "right":
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color("magenta")
        obstacle.penup()
        obstacle.goto(217.5, 290)
        things.append(obstacle)
        obstacles.append(obstacle)
    elif b1 == "obstacle" and a1 == "left":
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color("magenta")
        obstacle.penup()
        obstacle.goto(72.5, 290)
        things.append(obstacle)
        obstacles.append(obstacle)
    a2 = random.choice(["right", "left"])
    b2 = random.choice(["circle", "obstacle"])
#  to create the obstacles and circles in the left side of the screen
    if b2 == "circle" and a2 == "right":
        circle = turtle.Turtle()
        circle.shape("circle")
        circle.color("blue")
        circle.penup()
        circle.goto(-217.5, 250)
        things.append(circle)
        circles.append(circle)
    elif b2 == "circle" and a2 == "left":
        circle = turtle.Turtle()
        circle.shape("circle")
        circle.color("blue")
        circle.penup()
        circle.goto(-72.5, 250)
        things.append(circle)
        circles.append(circle)
    elif b2 == "obstacle" and a2 == "right":
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color("blue")
        obstacle.penup()
        obstacle.goto(-217.5, 250)
        things.append(obstacle)
        obstacles.append(obstacle)
    elif b2 == "obstacle" and a2 == "left":
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color("blue")
        obstacle.penup()
        obstacle.goto(-72.5, 250)
        things.append(obstacle)
        obstacles.append(obstacle)


f_create()


def go_left1():
    if carone.direction != "left":
        carone.direction = "left"


def go_right1():
    if carone.direction != "right":
        carone.direction = "right"


def go_left2():
    if cartwo.direction != "left":
        cartwo.direction = "left"


def go_right2():
    if cartwo.direction != "right":
        cartwo.direction = "right"


def start():
    global command
    if command != "start":
        command = "start"


def pause():
    global command
    if command != "pause":
        command = "pause"


wn.listen()
wn.onkeypress(go_left1,"a")
wn.onkeypress(go_right1,"d")
wn.onkeypress(go_left2,"j")
wn.onkeypress(go_right2,"l")
wn.onkeypress(start,"s")
wn.onkeypress(pause,"p")

#  function to move the cars to the right and left 
def move_cars():
    if carone.direction == "left":
        carone.goto(-217.5,-250)
    if carone.direction == "right":
        carone.goto(-72.5, -250)
    if cartwo.direction == "left":
        cartwo.goto(72.5, -250)
    if cartwo.direction == "right":
        cartwo.goto(217.5, -250)


def create():
     a1 = random.choice(["right","left"])
     b1 = random.choice(["circle","obstacle"])
     
     for index in range(len(things)):
          test = things[index - 1].ycor()
     
     if test < 150:
        #  to create the obstacles and the circles in the right of the screen
         if b1 == "circle" and a1 == "right":
             circle = turtle.Turtle()
             circle.shape("circle")
             circle.color("magenta")
             circle.penup()
             circle.goto(217.5, 290)
             things.append(circle)
             circles.append(circle)
         elif b1 == "circle" and a1 == "left":
             circle = turtle.Turtle()
             circle.shape("circle")
             circle.color("magenta")
             circle.penup()
             circle.goto(72.5, 290)
             things.append(circle)
             circles.append(circle)
         elif b1 == "obstacle" and a1 == "right":
             obstacle = turtle.Turtle()
             obstacle.shape("square")
             obstacle.color("magenta")
             obstacle.penup()
             obstacle.goto(217.5, 290)
             things.append(obstacle)
             obstacles.append(obstacle)
         elif b1 == "obstacle" and a1 == "left":
             obstacle = turtle.Turtle()
             obstacle.shape("square")
             obstacle.color("magenta")
             obstacle.penup()
             obstacle.goto(72.5, 290)
             things.append(obstacle)
             obstacles.append(obstacle)
        #  to create the obstacles and the circles in the left of the screen
         a2 = random.choice(["right", "left"])
         b2 = random.choice(["circle", "obstacle"])

         if b2 == "circle" and a2 == "right":
             circle = turtle.Turtle()
             circle.shape("circle")
             circle.color("blue")
             circle.penup()
             circle.goto(-217.5, 250)
             things.append(circle)
             circles.append(circle)
         elif b2 == "circle" and a2 == "left":
             circle = turtle.Turtle()
             circle.shape("circle")
             circle.color("blue")
             circle.penup()
             circle.goto(-72.5, 250)
             things.append(circle)
             circles.append(circle)
         elif b2 == "obstacle" and a2 == "right":
             obstacle = turtle.Turtle()
             obstacle.shape("square")
             obstacle.color("blue")
             obstacle.penup()
             obstacle.goto(-217.5, 250)
             things.append(obstacle)
             obstacles.append(obstacle)
         elif b2 == "obstacle" and a2 == "left":
             obstacle = turtle.Turtle()
             obstacle.shape("square")
             obstacle.color("blue")
             obstacle.penup()
             obstacle.goto(-72.5, 250)
             things.append(obstacle)
             obstacles.append(obstacle)


def move_obs():
    for index in range(len(things)):
        y = things[index].ycor()
        things[index].sety(y - 10)
    # rempve the old turtles
    if len(things) > 30:
        for i in range(10):
            things.pop(0)


def check_strike():
    global score
    global highscore

    # remove the old circles
    if len(circles) > 30:
        for i in range(8):
            circles.pop(0)
    
    for index in range(len(circles)-1,-1,-1):

        if circles[index].distance(carone) < 10:
            score += 1
            print("circle passd")
            cop = circles[index]
            cop.hideturtle()
            del circles[index]

            if score > highscore:
                highscore = score
            
            board.clear()
            board.write(f" Score : {score} \n  Highscore : {highscore}",align="center", font=("Courier", 16, "normal"))
        
        if circles[index].distance(cartwo) < 10:
            print("circlw passd")
            score += 1
            cop = circles[index]
            cop.hideturtle()
            del circles[index]
            
            if score > highscore:
                highscore = score
            
            board.clear()
            board.write(f" Score : {score} \n Highscore : {highscore}",align="center", font=("Courier", 16, "normal"))


    if len(obstacles) > 30:
        for i in range(8):
            obstacles.pop(0)
    
    global command
    
    for index in range(len(obstacles)-1,-1,-1):

        if obstacles[index].distance(carone) < 15:
            command = "over"

        if obstacles[index].distance(cartwo) < 15:
            command = "over"
    # to over the game if the circles pass the cars without touching
    # for index in range(len(circles)-1,-1,-1):
    #     if circles[index].ycor() < -290:
    #         command = "over"

while True:
    wn.update()
 
    if command == "start":
        n = 0
        paus.clear()
        new.clear()
        star.clear()
        move_obs()
        create()
        move_cars()
        check_strike()

    elif command == "pause":
        star.clear()
        paus.write("Press S to Resume", align="center", font=("Courier", 30, "normal"))

    elif command == "over":
        # Game over
        n += 1
        if n == 1: # to run the over command only once
        
            print("the car has been hit")
            new.write("       GAME OVER \n Press S to Start Again", align="center", font=("Courier", 30, "normal"))
            
            for i in range(len(things)-1):
                things[0].hideturtle()
                del things[0]
            
            for i in range(len(obstacles)-1):
                obstacles[0].hideturtle()
                del obstacles[0]
            
            for i in range(len(circles)-1):
                circles[0].hideturtle()
                del circles[0]

            f_create()
            if score > highscore:
                highscore = score
            score = 0
            board.clear()
            board.write(f" Score : {score} \n Highscore : {highscore}", align="center", font=("Courier", 16, "normal"))

    time.sleep(0.04)


wn.mainloop()


