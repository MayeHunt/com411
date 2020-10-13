def run():
  def display_ladder(steps):
    while(steps > 0):
      print("| |\n***")
      steps = steps - 1
    print("| |")

  def create_ladder():
    print("How many steps are there?")
    steps = int(input())
    display_ladder(steps)

  create_ladder() 