import matplotlib.pyplot as plt
import csv

def read_data():
  data = {} 
  with open("visual/subplots/temps.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    header = next(csv_reader)
    week1 = []
    week2 = [] 
    for row in csv_reader:
      week1.append(row[0].strip())
      week2.append(row[1].strip())
    data[header[0]] = week1
    data[header[1]] = week2
    
  return data 

def run():
  data = read_data() 

  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data['week1'])), data['week1'])
  ax2.plot(range(len(data['week2'])), data['week2'])
  plt.show()

  
run() 