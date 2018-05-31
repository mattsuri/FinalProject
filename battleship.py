#Matthew Suriawinata
#5/24/18
#battleship.py - it's battleship




from ggame import *
from random import randint

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 
white = Color(0xFFFFFF, 1) 


RADIUS = 50 #radius of circles
GAP = 100 #gap distance between circle centers
BORDEREDGE = 0 #border distance
DIAMETER = RADIUS * 2
BOARDSIZE = 5


def mouseClick(event):
    row = int((event.x - BORDEREDGE)/GAP)
    col = int((event.y - BORDEREDGE)/GAP)
    print(col)
    print(row)


def boardMartix():
    return [[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE]





if __name__ == "__main__":
    
    data = {}
   
    
    
    blackOutline = LineStyle(1, black)
    
    redCircle = CircleAsset(RADIUS, blackOutline, red)
    
    whiteCircle = CircleAsset(RADIUS, blackOutline, white) #radius, outline, fill
    for i in range (0,BOARDSIZE):
        height = BORDEREDGE + i*GAP
        for i in range (0,BOARDSIZE):
            Sprite(whiteCircle, (BORDEREDGE + i*GAP, height ))
            
            
    
    App().listenMouseEvent("click", mouseClick)

    App().run() 
