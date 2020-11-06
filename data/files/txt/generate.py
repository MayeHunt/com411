#import csv

def search(txtbooks):
  print("Searching...")
  data = dict() 
  with open(txtbooks) as file:
    section = ""
    for line in file:
      if line.startswith("Section:"):
        split = line.split(":")
        section = split[1].strip()
      else:
        if section in data:
          values = data[section]
          values.append(line.strip())
        else:
          data[section] = [line.strip()]
  print("Done!")
  return data 

def run(): 
  data = search("data/files/txt/books.txt")

  with open("data/files/txt/generated.csv", "w") as file:

    for value in data.items():
      section = value[0]
      books = value[1]

      for book in books:
        file.write(f"{section},{book}\n")
  #with open("generated.csv", "w", newline='') as csvfile:
    #csv_writer = csv.DictWriter(csvfile, fieldnames=data)
    
    #csv_writer.writeheader()
    #csv_writer.writerow(data)
    
    #for row in data:
      #csvfile
run() 