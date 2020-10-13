print("Program Started!")
print("Please enter a standard character:")
letter = input() 

if(len(letter) > 1):
  print("Only one character!")

if(len(letter) == 1):
  print("The ASCII code for",letter,"is",ord(letter))