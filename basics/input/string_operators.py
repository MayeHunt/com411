def run():
  print("Please enter the number of lives.")
  lives = int(input())
  print("\nPlease enter the energy level.")
  energy = int(input())
  print("\nPlease enter the shield level.")
  shield = int(input())
  print("\nHealth has been set.")

  print("Lives:", "♥" * lives)
  print("Energy:", "♦" * energy)
  print("Shield:", "♦" * shield)