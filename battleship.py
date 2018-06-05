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
BORDEREDGE = 0 #border distance
DIAMETER = RADIUS * 2
BOARDSIZE = 5
BOARDGAP = (DIAMETER*5) + DIAMETER

BLANK = 0 
SHIP = 1
MISS = 2 
HIT = 3


blackOutline = LineStyle(1, black)
    
redCircle = CircleAsset(RADIUS, blackOutline, red)
    
blankCircle = CircleAsset(RADIUS, blackOutline, white) #radius, outline, fill
hitCircle = CircleAsset(RADIUS, blackOutline, red) #radius, outline, fill
missCircle = CircleAsset(RADIUS, blackOutline, grey) #radius, outline, fill
shipCircle = CircleAsset(RADIUS, blackOutline, green) #radius, outline, fill

  
def mouseClick(event):
    col = int((event.x - BORDEREDGE)/DIAMETER)
    row = int((event.y - BORDEREDGE)/DIAMETER)
    compCol = int((event.x - BOARDGAP)/DIAMETER)
    compRow = int((event.y)/DIAMETER)
    print("col:", col)
    print("row:", row)
    print("compCol:", compCol)
    print("compRow:", compRow)
    
    if data["pickShips"] == True:
        if data["numShips"] < 6:
            if data["playerBoard"][row][col] != SHIP:
                    data["playerBoard"][row][col] = SHIP #assigning ship to spot in matrix
                    Sprite(shipCircle, (col*DIAMETER, row*DIAMETER))
                    data["numShips"] += 1
                    if data["numShips"] == 5:
                         data["pickShips"] = False
                         
   
    
    
    print(data["playerBoard"])
    
    redraw()

def buildBoard():
    return [[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE]


def redraw():
    
    for item in App().spritelist[:]: #Destroying sprites
        item.destroy()
    for row in range(0,BOARDSIZE): #the loop for board
        for column in range(0,BOARDSIZE):
            if data["playerBoard"][row][column] == BLANK:
                Sprite(blankCircle, (column*DIAMETER, row*DIAMETER))
            elif data["playerBoard"][row][column] == SHIP:
                Sprite(shipCircle, (column*DIAMETER, row*DIAMETER))
            elif data["playerBoard"][row][column] == MISS:
                Sprite(missCircle, (column*DIAMETER, row*DIAMETER))
            elif data["playerBoard"][row][column] == HIT:
                Sprite(hitCircle, (column*DIAMETER, row*DIAMETER))
    for row in range(0,BOARDSIZE): #the loop for board
        for column in range(0,BOARDSIZE):
            if data["compBoard"][row][column] == BLANK:
                Sprite(blankCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))
            elif data["compBoard"][row][column] == SHIP:
                Sprite(shipCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))
            elif data["comprBoard"][row][column] == MISS:
                Sprite(missCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))
            elif data["compBoard"][row][column] == HIT:
                Sprite(hitCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))


if __name__ == "__main__":
    
    data = {}
    data["numShips"] = 0 
    data["pickShips"] = True
    data["playerBoard"] = buildBoard()
    data["compBoard"] = buildBoard()
    
    
    redraw()
            
    
    App().listenMouseEvent("click", mouseClick)

    App().run() 
