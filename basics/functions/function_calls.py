def run():
  def display_box(word):
    print("---------------")
    print("|     "+word+"     |")
    print("---------------\n")


  def display_lower_case(word):
    print(word.lower())

  def display_upper_case(word):
    print(word.upper())

  def display_mirrored(word):
    result = word[::-1]
    print(result)

  def repeat(word,times):
    myboolean = True
    for x in range(times):
      if(myboolean == True):
        print(word.upper())
        myboolean = False
      elif(myboolean == False):
        print(word.lower())
        myboolean = True
    

  def runpls():
    print("Please enter a word")
    word = input() 
    print("Select and option:\nDisplay in a Box\nDisplay Lower-case\nDisplay Upper-case\nDisplay Mirrored\nRepeat")
    choice = input() 

    if(choice == 'display in a box'):
      display_box(word)
    elif(choice == 'display lower-case'):
      display_lower_case(word)
    elif(choice == 'display upper-case'):
      display_upper_case(word)
    elif(choice == 'display mirrored'):
      display_mirrored(word)
    elif(choice == 'repeat'):
      print("How many times would you like to repeat?")
      times = int(input()) 
      repeat(word,times)

  runpls()