def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  move = movements()
  for x in range(0,len(move),2):
    print("{} for {} steps".format(move[x],move[x+1]))

run()
