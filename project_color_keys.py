from turtle import *
from random import random
bgpic("water.png")
chase = Turtle()

#Screen / Drawing Setup
chase.width(10)
title("Color Keys!!!!")
textinput("Project Color Keys Instructions", "Use arrow keys to draw. You may change the colors using (r,g,b) as well as clear or undo using (Backspace, and c)")
chase.shape("turtle")
#Arrow Key Functions
def up_arrow():
    chase.fd(100)
def down_arrow():
    chase.back(100)
def left_arrow():
    chase.left(45)
def right_arrow():
    chase.right(45)

#Undo/Clear Functions
def back_space():
    chase.undo()
def clear_game():
    chase.clear()

#Color Functions
def red():
    chase.color(1,0,0)
def blue():
    chase.color(0,0,1)
def green():
    chase.color(0,1,0)
def space_bar():
    if chase.isdown():
        chase.penup()
    else:
        chase.pendown()




#Spacebar for controling the pen
onkeypress(space_bar, "space")
# Choose a color
#Press r for Red
#Press b for Blue
#Press g for Green
onkeypress(red, "r")
onkeypress(blue, "b")
onkeypress(green, "g")
# Undo/Clear
onkeypress(back_space, "BackSpace")
onkeypress(clear_game, "c")
# Draw with Arrow Keys
onkeypress(up_arrow, "Up")
onkeypress(down_arrow, "Down")
onkeypress(left_arrow, "Left")
onkeypress(right_arrow, "Right")
listen()
