class Human:
  #class attributes
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Human", age=0):
    #instance attributes
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  #instance methods
  def display(self):
    print(f"I am {self.name}")

#tester
if (__name__ == "__main__"):
  human = Human()
  human.display() 