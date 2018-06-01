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
grey = Color(0x787878, 1) 




RADIUS = 50 #radius of circles
GAP = 100 #gap distance between circle centers
BORDEREDGE = 0 #border distance
DIAMETER = RADIUS * 2
BOARDSIZE = 5

BLANK = 0 
SHIP = 1
MISS = 2 
HIT = 3


blackOutline = LineStyle(1, black)
    
redCircle = CircleAsset(RADIUS, blackOutline, red)
    
blankCircle = CircleAsset(RADIUS, blackOutline, white) #radius, outline, fill
hitCircle = CircleAsset(RADIUS, blackOutline, red) #radius, outline, fill
missCircle = CircleAsset(RADIUS, blackOutline, grey) #radius, outline, fill


def mouseClick(event):
    row = int((event.x - BORDEREDGE)/GAP)
    col = int((event.y - BORDEREDGE)/GAP)
    print(col)
    print(row)

    if data["pickShips"] == True:
        data["playerBoard"][row][col] == HIT
     

def buildBoard():
    return [[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE]


def redraw():
    
    for item in App().spritelist[:]: #Destroying sprites
        item.destroy()
    for row in range(0,BOARDSIZE): #the loop for board
        for column in range(0,BOARDSIZE):
            if data["playerBoard"][row][column] == BLANK:
                Sprite(blankCircle, (RADIUS+column*DIAMETER, RADIUS+row*DIAMETER))
            elif data["playerBoard"][row][column] == MISS:
                Sprite(missCircle, (RADIUS+column*DIAMETER, RADIUS+row*DIAMETER))
            elif data["playerBoard"][row][column] == HIT:
                Sprite(hitCircle, (RADIUS+column*DIAMETER, RADIUS+row*DIAMETER))
    


if __name__ == "__main__":
    
    data = {}
    data["numShips"] = 0 
    data["pickShips"] = True
    data["playerBoard"] = buildBoard()
    data["compBoard"] = buildBoard()
    
    
    redraw()
            
    
    App().listenMouseEvent("click", mouseClick)

    App().run() 
