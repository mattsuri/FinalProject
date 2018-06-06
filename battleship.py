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




RADIUS = 50 
BORDEREDGE = 0 #border distance
DIAMETER = RADIUS * 2
BOARDSIZE = 5
BOARDGAP = (DIAMETER*5) + DIAMETER # Distance between left edges of the boards


BLANK = 0 #Numerical assignments for the board matrices 
SHIP = 1
MISS = 2 
HIT = 3


blackOutline = LineStyle(1, black)
    
redCircle = CircleAsset(RADIUS, blackOutline, red)

    
blankCircle = CircleAsset(RADIUS, blackOutline, white) #radius, outline, fill
hitCircle = CircleAsset(RADIUS, blackOutline, red) #radius, outline, fill
missCircle = CircleAsset(RADIUS, blackOutline, grey) #radius, outline, fill
shipCircle = CircleAsset(RADIUS, blackOutline, green) #radius, outline, fill
#All circle types for ships

def compPick(): #computer picking after each mouseclick function
    row = randint(0,4)
    col = randint(0,4)
    
    if data["playerBoard"][row][col] != HIT and data["playerBoard"][row][col] != MISS:
        
        if data["playerBoard"][row][col] == SHIP:
            data["playerBoard"][row][col] = HIT
            data["compHits"] += 1
            
        elif data["playerBoard"][row][col] == BLANK:
            data["playerBoard"][row][col] = MISS
            
    else:
        compPick()
            
        
  
  
def mouseClick(event):
    if data["play"] == True:
        col = int((event.x - BORDEREDGE)/DIAMETER) #finding row and col in terms of boards by divding by diameter 
        row = int((event.y - BORDEREDGE)/DIAMETER)
        compCol = int((event.x - BOARDGAP)/DIAMETER)
        compRow = int((event.y)/DIAMETER)
        
        if data["pickShips"] == True: #allow player to pick ships initial unitl max ship limit is reached
            if data["numShips"] < 6:
                if data["playerBoard"][row][col] != SHIP:
                        data["playerBoard"][row][col] = SHIP #assigning ship to spot in matrix
                        data["numShips"] += 1
                        if data["numShips"] == 5:
                             data["pickShips"] = False
                             
                             
        else: #changing classifications/values in the compBoard matrix to respond to click locations
            if event.x > BOARDGAP:
                if data["compBoard"][compRow][compCol] != MISS and data["compBoard"][compRow][compCol] != HIT:
                    compPick()
                    if data["compBoard"][compRow][compCol] == BLANK:
                        data["compBoard"][compRow][compCol] = MISS
                        
                    elif data["compBoard"][compRow][compCol] == SHIP:
                        data["compBoard"][compRow][compCol] = HIT
                        data["playerHits"] += 1
                        
        
        redraw()


def compShipPick(): #allows computer to pick ship in the beginning 
    while data["compShips"] < 5:
        row = randint(0,4)
        col = randint(0,4)
        if data["compBoard"][row][col] != SHIP:
            data["compBoard"][row][col] = SHIP
            data["compShips"] += 1
            



def buildBoard(): #makes a blank board based on the BOARDSIZE
    return [[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE,[BLANK]*BOARDSIZE]


def redraw():
    
    for item in App().spritelist[:]: #Destroying sprites
        item.destroy()
    for row in range(0,BOARDSIZE): #the loop for refreshing player board
        for column in range(0,BOARDSIZE):
            if data["playerBoard"][row][column] == BLANK:
                Sprite(blankCircle, (column*DIAMETER, row*DIAMETER))
            elif data["playerBoard"][row][column] == SHIP:
                Sprite(shipCircle, (column*DIAMETER, row*DIAMETER))
            elif data["playerBoard"][row][column] == MISS:
                Sprite(missCircle, (column*DIAMETER, row*DIAMETER))
            elif data["playerBoard"][row][column] == HIT:
                Sprite(hitCircle, (column*DIAMETER, row*DIAMETER))
    for row in range(0,BOARDSIZE): #the loop for refreshing computer board
        for column in range(0,BOARDSIZE):
            if data["compBoard"][row][column] == BLANK:
                Sprite(blankCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))
            elif data["compBoard"][row][column] == SHIP:
                Sprite(blankCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))
            elif data["compBoard"][row][column] == MISS:
                Sprite(missCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))
            elif data["compBoard"][row][column] == HIT:
                Sprite(hitCircle, (column*DIAMETER+BOARDGAP, row*DIAMETER))

    
    Sprite(TextAsset(data["playerHits"], fill = black, style = "Bold 24pt Times"), (145,DIAMETER*5))
    Sprite(TextAsset(data["compHits"], fill = black, style = "Bold 24pt Times"), (800,DIAMETER*5))
    Sprite(TextAsset("PLAYER:", fill = black, style = "Bold 24pt Times"),(DIAMETER*0,DIAMETER*5))
    Sprite(TextAsset("COMPUTER:", fill = black, style = "Bold 24pt Times"),(DIAMETER*6,DIAMETER*5))
    
    if data["playerHits"] == 5: #check to see if anyone has hit all the hips
        data["play"] = False #Stops mouse function from running after game ends
        Sprite(TextAsset("YOU WIN", fill = black, style = "Bold 60pt Times"),(325,150))
    elif data["compHits"] == 5:
        data["play"] = False
        Sprite(TextAsset("YOU LOSE", fill = black, style = "Bold 60pt Times"),(325,150))

if __name__ == "__main__":
    
    data = {}
    data["play"] = True
    data["numShips"] = 0
    data["compShips"] = 0
    data["pickShips"] = True
    data["playerHits"] = 0
    data["compHits"] = 0 
    data["playerBoard"] = buildBoard()
    data["compBoard"] = buildBoard()
    data["compPickShips"] = False
    
   
    redraw()
    compShipPick()
            
    print("Choose where to place 5 ships on the PLAYER board then proceed to guess the location of the enemy's ships on the COMPUTER board")
    
    App().listenMouseEvent("click", mouseClick)

    App().run() 
