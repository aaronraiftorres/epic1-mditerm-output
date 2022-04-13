from colorsys import rgb_to_hls
from ctypes.wintypes import RGB
import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(0)



def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4
        
def drawdesign():
    turtle.color("indigo")
    for i in range(10):
        drawcircle(150)
        turtle.right(36)
        
        
def torres():
    turtle.color("violet")
    for i in range(10):
        turtle.circle(155)
        turtle.right(36)
        
def berthday():
    turtle.color("magenta")
    for i in range(10):
        turtle.circle(160)
        turtle.right(36)
        

def secondlayer():
    turtle.color("pink")
    for i in range(17):
         turtle.circle(130)
         turtle.right(100)
         

         
def twins():
    turtle.color("violet")
    for i in range(6):
         drawcircle(110)
         turtle.right(60)
         
def raif():
    turtle.color("white")
    for i in range(17):
        turtle.circle(90)
        turtle.right(100)
        

drawdesign()
torres()
berthday()
secondlayer()
twins()
raif()





turtle.hideturtle()
turtle.done()