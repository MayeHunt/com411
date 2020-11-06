def search(txtbooks):
  print("Searching...")
  sections = [] 
  books = [] 
  with open(txtbooks) as txtbooks:
    for line in txtbooks:
      if line.startswith("Section:"):
        split = line.split(":")
        sections.append(split[1].replace("\n","") + ", ")
      else:
        books.append(line.replace("\n","") + ", ")
  print("Done!")
  return (sections,books)

def save(savefile,data):
  print("Saving...")
  with open(savefile, "w") as file:
    file.write("Sections: ")
    for x in range(len(data[0])):
      if (x < len(data[0]) -1):
        file.write(f"{data[0][x]},")
      else:
        file.write(f"{data[0][x]}")

    file.write("\nBooks: ")
    for x in range(len(data[1])):
      if (x < len(data[1]) - 1):
        file.write(f"{data[1][x]},")
      else:
        file.write(f"{data[1][x]}")
  print("Done!")

def run(): 
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data) 

run() 
