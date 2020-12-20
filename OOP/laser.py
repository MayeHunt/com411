from tech import Tech

class Laser(Tech):


  def activate():
    print("Laser Activated!")

  
  def fire(range):
    print(f"Shoots at a range of {range}!")

  
  def deactivate(): 
    print("Laser Shutting Down...")


if (__name__ == "__main__"):
  Laser.activate() 
  Laser.fire(100)
  Laser.deactivate()
