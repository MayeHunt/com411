def run():
  print("What type of cover does the book have? (hard or soft)")
  cover = input() 

  if(cover == 'soft'):
    print("Is the book perfect-bound?")
    bound = input() 
    if(bound == 'yes'):
      print("Softer cover, perfect bound books are very popular!")
    else:
      print("Soft covers with coils or stitches are great for short books!")
  elif(cover == 'hard'):
    print("Books with hard covers can be more expensive!")

