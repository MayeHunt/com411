from tech import Tech

class Jetpack(Tech):


  def activate():
    print("Jetpack Activated!")


  def fly(speed):
    print(f"Flying at a speed of {speed}!")

  
  def deactivate(): 
    print("Jeckpack Shutting Down...")


if (__name__ == "__main__"):
  Jetpack.activate() 
  Jetpack.fly(100)
  Jetpack.deactivate()
  