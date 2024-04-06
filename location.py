import random


class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def getRandLoc(maxX, maxY):
        rand_x = random.randint(0,maxX)
        rand_y = random.randint(0,maxY)
        return Location(rand_x, rand_y)

    
    def setLoc(self,x1,y1):
        self.x = x1
        self.y = y1
    
    def delta(self,dx,dy, maxX, maxY):
        # print("dxdy: ", dx,dy)
        # print("maxes: ", maxX, maxY)
        # print("before", self.x, self.y)
        # print("min pre", (dx+self.x, maxX), (dy+self.y, maxY))
        # print("min post", min(dx+self.x, maxX), min(dy+self.y, maxY))
        # print("max pre", (0,min(dx+self.x, maxX)), (0,min(dy+self.y, maxY)))
        # print("max post", max(0,min(dx+self.x, maxX)), max(0,min(dy+self.y, maxY)))
        
        new_x = dx+self.x
        new_y = dy+self.y
        
        if new_x <0 or new_y < 0 or new_x > maxX or new_y > maxY:
            return False
        
        self.x = new_x
        self.y = new_y
        return True
        # print("after", self.x, self.y)

 
 
 