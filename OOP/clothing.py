from clothing_size import Clothing_size

class Clothing:

  
  def __init__(self, colour, material, size):
    self.colour = colour
    self.material = material
    self.size = size 


if (__name__ == "__main__"):
  red_silk = Clothing("Red", "Silk", Clothing_size.MEDIUM)

