import random 

OPTIONS = ["rock", "paper", "scissors"]

while True:
  print("Make your throw")
  userOption = input(" Please type rock, paper or scissors: ")
  if userOption in OPTIONS:
      computerOption = random.choice(OPTIONS)
      print(
          f"\nYou threw '{userOption}', the computer threw '{computerOption}' "
      )
  else:
      print(f"\nYou typed '{userOption}' which is not a valid throw")  

  throwAgain = input("\n Ready for another round? (y/n): ")
  if throwAgain.lower() == "n": 
      break
  
  print()

  
print("\n Bye-bye! See you next time!")