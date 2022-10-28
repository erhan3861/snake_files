from turtle import *

wn = Screen()
wn.title("Snake Game")
wn.bgcolor("black")

for i in range(0, 15):
  wn.addshape("frame_0" + str(0) + "_delay-0.2s.gif")


player = Turtle()
player.shape("frame_00_delay-0.2s.gif")