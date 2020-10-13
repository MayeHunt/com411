def run():
  print("Program Started!")
  print("Please enter an ASCII code:")

  code = abs(int(input()))

  if(code in range(32,126)):
    print("The character represented by the ASCII code",code,"is",chr(code))
  else:
    print("Please enter a valid ASCII code.")

  print("Program ended!")