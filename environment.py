import sys
from organism import Organism
import random
from location import Location

class Environment:

  def __init__(self, width, height):
    self.ticks = 0
    self.height = int(height)
    self.width = int(width)
    self.organisms = []
    self.goal = Location.getRandLoc(self.width-1, self.height-1)
    self.addRandomOrganism()
    
    
  def addRandomOrganism(self):
    self.organisms.append(Organism(self))

  def tickTime(self):
    for organism in self.organisms:

      if organism.loc.x == self.goal.x and organism.loc.y == self.goal.y:
        return 1
      
      if not organism.doAction(self.goal):
        return -1
      
    self.ticks +=1
    return 0
  
  def loadWeights(self, filename):
    for organism in self.organisms:
      organism.loadWeights(filename)
  
  def getWeights(self):
    for organism in self.organisms:
      return organism.getWeights()
  
  def relocateOrganism(self):
    for organism in self.organisms:
      organism.relocate()
      
  def relocateGoal(self):
    self.goal = Location.getRandLoc(self.width-1, self.height-1)
    
  def resetEnvironment(self):
    self.organisms.clear()

  def toString(self):
    grid = [[None for i in range(self.width)] for j in range(self.height)]

    for org in self.organisms:
      grid[org.loc.y][org.loc.x] = org
    
    stringBuilder = " "+"--"*self.width + "\n"
    for y in range(self.height):
      stringBuilder += "|"
      for x in range(self.width):
        
        if grid[y][x] == None:
          if x == self.goal.x and y == self.goal.y:
            stringBuilder += "+"
          else:
            stringBuilder += " "
        else:
          stringBuilder += grid[y][x].toString()

        stringBuilder += " "
      stringBuilder += "|"
      stringBuilder += "\n"
    stringBuilder +=  " "+"--"*self.width
      

    return stringBuilder

