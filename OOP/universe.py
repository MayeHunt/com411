from planet import Planet
from robot import Robot
from human import Human
import random 

class Universe: 

  #initialiser
  def __init__(self):
    #instance variable
    self.planets = []

  #instance methods
  def generate(self):
    #create new planet object
    planet = Planet()

    #add random number of humans & robots to planet object (loop + random)
    for x in range(random.randint(1,10)):
      robot = Robot(f"Robot{x}")
      planet.add_robot(robot)

    for x in range(random.randint(1,10)):
      human = Human(f"Human{x}")
      planet.add_human(human)

    #adds planet object to list of planets
    self.planets.append(planet) 

  #magic methods
  def __repr__(self): 
    return f"Planets:{self.planets}"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets."

if (__name__ == "__main__"):
  universe = Universe() 
  universe.generate() 
  print(repr(universe))
  universe.generate()
  print(repr(universe))
  print(universe)
  