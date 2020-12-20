from abc import ABC

class Inhabitant(ABC):

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0):
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY


  #magic methods
  def __repr__(self):
    return f'inhabitant(name={self.name}, age={self.age}, energy={self.energy})'


  def __str__(self):
    return f'inhabitant: {self.name} is {self.age} years old and their energy is {self.energy}.'


  #instance methods
  def grow(self):
    self.age += 1


  def eat(self,amount):
    totalEnergy = self.energy + amount
    if(totalEnergy > Inhabitant.MAX_ENERGY):
      self.energy = Inhabitant.MAX_ENERGY
      return totalEnergy - self.energy
    else:
      self.energy = totalEnergy
      return 0


  def move(self,distance):
    moveEnergy = self.energy - distance
    if(moveEnergy < 0):
      self.energy = 0
      return self.energy - moveEnergy
    else:
      self.energy = moveEnergy
      return 0


if (__name__ == "__main__"):
  inhabitant = Inhabitant()
  inhabitant.display() 
  print(repr(inhabitant))  