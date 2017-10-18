from turtle import *
from random import randint
from random import random
chase = Turtle()

bgpic("water.png")
bgpic()

le = 5
width = 10
chase.shape("turtle")
chase.speed(20)

for i in range(750):
    chase.width(width)
    chase.fd(5)
    chase.color(random(), random(), random())
    chase.left(45)
    chase.fd(le)
    le = le + 1









 
