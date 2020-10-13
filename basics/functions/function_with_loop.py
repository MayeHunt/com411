def cross_bridge(distance):
  steps = 0
  while(distance > 0):     
    print("Crossed step")
    distance = distance - 1
    steps = steps + 1
  if(steps > 5):
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

cross_bridge(3) 
cross_bridge(6) 