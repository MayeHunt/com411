class Robot:
  #class attributes
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Robot", age=0):
    #instance attributes
    self.name = name
    self.age = age
    self.energy = 0

  #magic methods
  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'
  def __str__(self):
    return f'Robot: {self.name} is {self.age} years old and its energy is {self.energy}.'

  #instance methods
  def display(self):
    print(f"I am {self.name}")

#tester
if (__name__ == "__main__"):
  robot = Robot()
  robot.display() 
  print(repr(robot))
  print(str(robot))