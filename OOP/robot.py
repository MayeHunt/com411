class Robot:
  #class attributes
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Robot", age=0):
    #instance attributes
    self.name = name
    self.age = age
    self.energy = Robot.MAX_ENERGY

  #magic methods
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'
  def __str__(self):
    return f'Robot: {self.name} is {self.age} years old and its energy is {self.energy}.'

  #instance methods
  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat(self,amount):
    totalEnergy = self.energy + amount
    if(totalEnergy > Robot.MAX_ENERGY):
      self.energy = Robot.MAX_ENERGY
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
  robot = Robot()
  robot.display() 
  print(repr(robot))
  robot.grow() 
  robot.eat(10)
  robot.move(50)
  print(repr(robot))
  robot.grow() 
  robot.eat(10)
  robot.move(50)
  print(repr(robot))