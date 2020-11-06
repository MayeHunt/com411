def search(locations):
  print("Searching...")
  with open(locations) as file:
    for line in file:
      print(f"Looked in {line}", end = "")
    print("\n...Done!")

def run():
  search("data/files/txt/locations.txt")

run() 