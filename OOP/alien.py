from inhabitant import Inhabitant

class Alien(Inhabitant):


  #initialiser
  def __init__(self, name="Alien", age=0):
    super().__init__(name, age)


  #magic methods
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'
  def __str__(self):
    return f'Human: {self.name} is {self.age} years old and their energy is {self.energy}.'

  #instance methods
  def display(self):
    print(f"I am {self.name}")