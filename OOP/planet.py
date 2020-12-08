from human import Human
from robot import Robot

class Planet:

  #initialiser
  def __init__(self):
    self.inhabitants = {
    'humans' : [],
    'robots' : [] 
    }

  #instance methods
  def add_human(self, human):
    self.inhabitants['humans'].append(human)

  def remove_human(self, human):
    self.inhabitants['humans'].remove(human)

  def add_robot(self, robot):
    self.inhabitants['robots'].append(robot)
    
  def remove_robot(self,robot):
    self.inhabitants['robots'].remove(robot)

  #magic methods
  def __repr__(self):
    return f"Humans:{self.inhabitants['humans']}\nRobots:{self.inhabitants['robots']}"

  def __str__(self):
    return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."

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
  planet.remove_human(jeff) 
  planet.remove_robot(maye) 

  print(planet)