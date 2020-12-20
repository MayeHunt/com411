from human import Human
from robot import Robot

class Planet:


  #initialiser
  def __init__(self):
    self.inhabitants = []


  #instance methods
  def add_inhabitant(self, inhabitant):
    self.inhabitants.append(inhabitant)


  def remove_inhabitant(self, inhabitant):
    self.inhabitants.remove(inhabitant)


  #magic methods
  def __repr__(self):
    return f"Inhabitants:{self.inhabitants}"


  def __str__(self):
    return f"This planet has {len(self.inhabitants)} inhabitants"


#testers
if (__name__ == "__main__"):
  planet = Planet()
  print(repr(Planet))

  #add inhabitants
  jeff = Human("Jeff")
  planet.add_inhabitant(jeff)
  seb = Human("Seb")
  planet.add_inhabitant(seb)
  ari = Human("Ari")
  planet.add_inhabitant(ari)
  maye = Robot("Maye")
  planet.add_inhabitant(maye)

  print(repr(planet))

  #remove humans & robots
  planet.remove_inhabitant(jeff) 

  print(planet)
