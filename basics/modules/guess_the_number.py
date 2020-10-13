def run():
  import random as rnd

  def play_guess_the_number(number):
    mybool = False
    while(mybool == False):
      guess = int(input()) 
      if(guess == number):
        print("Congratulations! You guessed my number!")
        mybool = True
      elif(guess > number):
        print("Your guess is too high.")
      elif(guess < number):
        print("Your guess is too low.")
      else:
        print("Try again:")


  print("Please enter the minimum value:")
  minimum = int(input()) 
  print("Please enter the maximum value:")
  maximum = int(input()) 

  number = rnd.randrange(minimum,maximum)

  print("I am thinking of a number between",str(minimum),"and",str(maximum)+". Can you guess what it is?")

  play_guess_the_number(number)