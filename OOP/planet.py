from human import Human
from robot import Robot

class Planet:

  #initialiser
  def __init__(self):
    self.humans = [] 
    self.robots = [] 

  #instance methods
  def add_human(self, human):
    self.humans.append(human)

  def remove_human(self, human):
    self.humans.remove(human)

  def add_robot(self, robot):
    self.robots.append(robot)
    
  def remove_robot(self,robot):
    self.robots.remove(robot)

  #magic methods
  def __repr__(self):
    return f'Humans:{self.humans}\nRobots:{self.robots}'

  def __str__(self):
    return f'This planet has {len(self.humans)} humans and {len(self.robots)} robots.'

#testers
if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))

  #add humans
  jeff = Human("Jeff")
  planet.add_human(jeff)
  seb = Human("Seb")
  planet.add_human(seb)
  ari = Human("Ari")
  planet.add_human(ari)

  #add robots
  maye = Robot("BeepBoopMaye")
  planet.add_robot(maye) 
  frank = Robot("BeepBoopFrank")
  planet.add_robot(frank)

  print(repr(planet))

  #remove humans & robots
  planet.remove_human("Jeff") 
  planet.remove_robot("BeepBoopMaye") 

  print(planet)