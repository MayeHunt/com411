import matplotlib.pyplot as plt

def read_data(file):
  with open(file) as file:
    temps = [] 
    for line in file:
      temps.append(int(line.strip()))
  return temps 

def run():
  data = read_data("visual/subplots/temps.txt")
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data)), data)
  ax2.bar(range(len(data)), data)
  plt.show()

run()