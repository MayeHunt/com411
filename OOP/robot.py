class Robot:
  #class attributes
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Robot", age=0):
    #instance attributes
    self.name = name
    self.age = age
    self.energy = 0

  #instance methods
  def display(self):
    print(f"I am {self.name}")

#tester
if (__name__ == "__main__"):
  robot = Robot()
  robot.display() 