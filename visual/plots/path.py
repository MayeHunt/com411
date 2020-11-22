import matplotlib.pyplot as plt

def coordinate():
  print("Enter an x value:")
  x = input() 
  print("Enter a y value:")
  y = input() 
  return (x,y) 

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for _ in range(4):
    coordinates = coordinate() 
    x_values.append(coordinates[0])
    y_values.append(coordinates[1])
  return [x_values,y_values]

def run():
  values = path()
  plt.plot(values[0],values[1],'ro--')
  plt.show()

run() 