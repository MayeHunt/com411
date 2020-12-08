class Human:
  #class attributes
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Human", age=0):
    #instance attributes
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  #magic methods
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'
  def __str__(self):
    return f'Human: {self.name} is {self.age} years old and their energy is {self.energy}.'

  #instance methods
  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat(self,amount):
    totalEnergy = self.energy + amount
    if(totalEnergy > Human.MAX_ENERGY):
      self.energy = human.MAX_ENERGY
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

#tester
if (__name__ == "__main__"):
  human = Human()
  human.display() 
  print(repr(human))
  human.grow() 
  human.eat(10)
  human.move(50)
  print(repr(human))
  human.grow() 
  human.eat(10)
  human.move(50)
  print(repr(human))