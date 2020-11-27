import matplotlib.pyplot as plt
import csv

def read_data():
  with open("visual/subplots/titanic.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    header = next(csv_reader)
    data = {'survived':[], 'age':[]}

    for line in csv_reader:
      survived = line[1].strip()
      age = line[4].strip()

      if (survived != "" and age != ""):

        data['survived'].append(bool(int(survived)))
      
        data['age'].append(float(age))



  return data

def run():
  data = read_data()

  fig, (ax1) = plt.subplots(1)
  ax1.bar(data['age'],data['survived'])
  plt.show()


run()