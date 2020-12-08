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

#tester
if (__name__ == "__main__"):
  human = Human()
  human.display() 
  print(repr(human))
  print(str(human))