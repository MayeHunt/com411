from inhabitant import Inhabitant

class Human(Inhabitant):
  #class attributes
  MAX_ENERGY = 100

  #initialiser
  def __init__(self, name="Human", age=0):
    super().__init__(name, age)


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
  human.grow() 
  human.eat(10)
  human.move(50)
  print(repr(human))
  human.grow() 
  human.eat(10)
  human.move(50)
  print(str(human))