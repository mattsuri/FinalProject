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


def compPick():
    row = randint(0,4)
    col = randint(0,4)
    i = 0 
    while i < 1:
        if data["playerBoard"][row][col] != HIT or data["playerBoard"][row][col] != MISS:
            if data["playerBoard"][row][col] == SHIP:
                data["playerBoard"][row][col] = HIT
                i += 1
            elif data["playerBoard"][row][col] == BLANK:
                data["playerBoard"][row][col] = MISS
                i += 1
            
        
  
  
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
                    
                    data["numShips"] += 1
                    if data["numShips"] == 5:
                         data["pickShips"] = False
                         data["compPickShips"] = True
                         
   
    else:
        if data["compBoard"][compRow][compCol] != MISS and data["compBoard"][compRow][compCol] != HIT:
            compPick()
            if data["compBoard"][compRow][compCol] == BLANK:
                data["compBoard"][compRow][compCol] = MISS
                
            elif data["compBoard"][compRow][compCol] == SHIP:
                data["compBoard"][compRow][compCol] = HIT
                data["playerHits"] += 1
                
            
    
    print(data["playerBoard"])
    
    redraw()


def compShipPick():
    i = 0
    while i < 5:
        row = randint(0,4)
        col = randint(0,4)
        if data["compBoard"][row][col] != SHIP:
            data["compBoard"][row][col] = SHIP
            i += 1



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
            elif data["compBoard"][row][column] == MISS:
                Sprite(missCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))
            elif data["compBoard"][row][column] == HIT:
                Sprite(hitCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))


if __name__ == "__main__":
    
    data = {}
    data["numShips"] = 0
    data["compShips"] = 6
    data["pickShips"] = True
    data["playerHits"] = 0
    data["playerBoard"] = buildBoard()
    data["compBoard"] = buildBoard()
    data["compPickShips"] = False
    
    redraw()
    compShipPick()
            
    
    App().listenMouseEvent("click", mouseClick)

    App().run() 
