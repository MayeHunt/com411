def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  move = movements()
  int0 = 0
  int1 = 1
  while int0 <= 6:
    print("{} for {} steps".format(move[int0],move[int1]))
    int0 = int0 + 2
    int1 = int1 + 2
run()