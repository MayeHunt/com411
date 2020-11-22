import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {} 
  print("Pick a line type :, --, or -")
  line = input() 
  print("Pick a colour r, g, or b")
  colour = input() 
  print("Pick a marker style o, s, or ^")
  marker = input() 
  paths['line'] = line.strip()
  paths['colour'] = colour.strip()
  paths['marker'] = marker.strip()
  return paths 

def generate(): 
  print("How many lines would you like to display?")
  lines = int(input()) 
  for _ in range(lines):
    values = data() 
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    format = f"{values['colour']}{values['line']}{values['marker']}"
    plt.plot(x,y,format)
    
  plt.show() 

def run():
  print("Running...")
  generate()
  print("Done!")

run()