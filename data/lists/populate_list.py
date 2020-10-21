def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  menu = directions() 
  for x in range(len(menu)):
    print("{}: {}".format(x,menu[x]))
  choice = int(input()) 
  return menu[choice]

def run():
  route = []
  print("Working out escape route...")
  for x in range(0,5,1):
    choice = menu() 
    route.append(choice)
  print(route)

run() 