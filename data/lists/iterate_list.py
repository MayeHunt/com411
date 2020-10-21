def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  menu = directions() 
  for x in range(len(menu)):
    print("{}: {}".format(x,menu[x]))

def run():
  menu() 

run() 