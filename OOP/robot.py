from inhabitant import Inhabitant

class Robot(Inhabitant):
  #class attributes
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Robot", age=0):
    super().__init__(name, age)

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
  robot.grow() 
  robot.eat(10)
  robot.move(50)
  print(repr(robot))
  robot.grow() 
  robot.eat(10)
  robot.move(50)
  print(repr(robot))