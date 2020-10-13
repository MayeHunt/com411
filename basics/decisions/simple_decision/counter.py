def run():
  print("Please enter the first whole number.")
  num1 = int(input()) 
  print("Please enter the second whole number.")
  num2 = int(input()) 
  print("Please enter the third whole number.")
  num3 = int(input()) 

  odd = 0
  even = 0

  if(num1 % 2 == 1):
    odd = odd + 1
  else:
    even = even + 1

  if(num2 % 2 == 1):
    odd = odd + 1
  else:
    even = even + 1

  if(num3 % 2 == 1):
    odd = odd + 1
  else:
    even = even + 1

  print("There were",even,"even numbers and",odd,"odd numbers.")