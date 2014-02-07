__author__ = 'gkline'
import turtle
# myColor= input("What background color do you want to use?")
# tessColor = input("What color do you want tess to be?")
TessPen = input("How big do you want the pen to be? ")
int(TessPen)
wn = turtle.Screen()
wn.bgcolor("SteelBlue4")
tess = turtle.Turtle()
tess.color("yellow1")
tess.pensize(TessPen)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
