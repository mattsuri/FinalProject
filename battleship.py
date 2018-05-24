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
GAP = 50 #gap distance between circle centers
BORDEREDGE = 50 #border distance
DIAMETER = 200



if __name__ == "__main__":
    
    data = {}
   
    
    
    blackOutline = LineStyle(1, black)
    
    redCircle = CircleAsset(RADIUS, blackOutline, red)
    
    whiteCircle = CircleAsset(RADIUS, blackOutline, white) #radius, outline, fill
    for i in range (0,10):
        height = BORDEREDGE + i*GAP
        for i in range (0,10):
            Sprite(whiteCircle, (BORDEREDGE + i*GAP, height ))
            
            
    
 
    App().run() 
