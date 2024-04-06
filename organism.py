from location import Location
from brain import Brain

class Organism:
  def __init__(self, environment, location=None, energy=0):
      self.energy = energy
      self.environment = environment
      self.brain = Brain(True)

      if location is None:
          self.loc = Location.getRandLoc(environment.width-1, environment.height-1)
          return
      else:
          self.loc = location

  def loadWeights(self, filename):
    self.brain.nn.readWeights(filename)

  def relocate(self):
    self.loc = Location.getRandLoc(self.environment.width-1, self.environment.height-1)
  
  def getWeights(self):
    return [self.brain.nn.weights, self.brain.nn.layers]

  def toString(self):
    stringBuilder = str(self.energy)
    return stringBuilder
  
  def doAction(self, goal: Location):
    x = self.loc.x
    y = self.loc.y
    goal_x = goal.x
    goal_y = goal.y
    n = self.brain.doAction([x, y, goal_x, goal_y])
    # #n: 0-5, make a -1 - 1
    # if(n==0):
    #   dx = ((n-1)%2) - ((n-1)//2)
    #   dy = ((n)%2) - ((n-1)//2)
    
    # return self.move(n[0],n[1])
    return self.loc.delta(n[0],n[1], self.environment.width-1, self.environment.height-1)

      
  # def move(self, dx, dy):
  #   return self.loc.delta(dx, dy)
    
    

    
  
  
    
      
    
    


