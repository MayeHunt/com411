from inhabitant import Inhabitant
from clothing import Clothing

class Human(Inhabitant):


  #initialiser
  def __init__(self, name="Human", age=0):
    super().__init__(name, age)
    self.clothes = []


  #magic methods
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'
  def __str__(self):
    return f'Human: {self.name} is {self.age} years old and their energy is {self.energy}.'

  #instance methods
  def display(self):
    print(f"I am {self.name}")


  def clothing(self):
    if self.clothes == []:
      print(f"This human is wearing nothing!")
    else:
      print(f"This human is wearing {self.clothes}.")


  def dress(self, colour, material, size):
    clothes = Clothing(colour, material, size)
    self.clothes.append(clothes)
    print(clothes)

  def undress(self):
    clothes = Clothing.__init__()
    self.clothes.remove(clothes)

 
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

  #clothes.append(Clothing.__init__("red", "cloth", Clothing_size.SMALL))
  human.clothing()
  human.dress("red", "cloth", 1)
  human.clothing()
