
import random
import os

def user_move():
  os.system("cls")
  print(" ")
  print(" R) for Rock")
  print(" P) for Paper")
  print(" S) for Scissors","\n")
  user = input("Press the letter ")
  user = user.lower()
  return user

def comp_move():
  choose_one = ["rock" ,"paper" ,"scissors"]
  choose_one = random.choice(choose_one)
  return choose_one
  
def rock():
  print(" ")
  print("             ▄▄▄▄             ")
  print("      ▄▀▀▀▀▄▀    ▀▄▀▀▀▄       ")
  print("  ▄▀▀▀█    ▀      ▀     █     ")
  print("  █              ▄      █     ")
  print("  █   ▄    █     █      █     ")
  print("  █   █    █     █      █▄    ")
  print("  █   █    █     █      █▀▄   ")
  print("   ▀▀▀ ▀▄▄▄▀▄    █▄    ▄▀ █   ")
  print("             █▀▀▀▄ ▀▀▀▀   ▄█  ")
  print("              ▀▄▄▄█▄▄▄▄▄▄▀    ")
  
def paper():
  print(" ")
  print("               ▄▄             ")
  print("          ▄▄  █  █  ▄▄        ")
  print("         █  █ █  █ █  █  ▄▄   ")
  print("         █  █ █  █ █  █ █  █  ")     
  print("         █  █ █  █ █  █ █  █  ")
  print("         █  █ █  █ █  █ █  █  ")
  print("   ▄▄    █   ▀    ▀    ▀█  █  ")
  print("  █  ▀▄  █                 █  ")
  print("  ▀▄  ▀▄ █                 █  ")
  print("   ▀▄  ▀▄█                 █  ")
  print("    ▀▄                    ▄▀  ")
  print("      ▀▄                 ▄▀   ")
  print("        ▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀     ")

def scissors():
  print(" ")
  print("  ▄▀▄                         ")
  print(" █   ▀▄         ▄▀▀▄          ")
  print("  ▀▄   ▀▄    ▄▀▀    ▀▀▄       ")
  print("    ▀▄   ▀▄▄▀         ▀▀▄     ")
  print("      ▀▄   █  ▄▀▀▄       ▀▀▄  ")
  print("      ▄▀   █  █  ▀▄▄       █  ")
  print("    ▄▀     █  █            █  ")
  print("  ▄▀   ▄▀▀▀█ ▄▀▄▄▄▄▄▄      █  ")
  print(" █   ▄▀   █ ▀        █     █  ")
  print("  ▀▄▀     ▄▀▀▀▀▀▀▀▀▀▀▄    ▄▀  ")
  print("          ▀▄▄▄▄▄▄▄▄▄▄▀  ▄▀    ")
  print("               ▀▀▀▀▀▀▀▀▀      ")  

def inp_user():
  print(" ")
  print("   This is the user's move   ")

def inp_comp():
  print(" ")
  print("   This is the computer's move   ")

print(" ")
Keep_going = input("Do you want to play? ")
Keep_going = Keep_going.lower()

hu = 0
co = 0
while Keep_going == "yes":
  human = user_move()
  while human != "r" and human != "p" and human != "s":
    os.system("cls")
    human = user_move()
    
  if human == "r":
    os.system("cls")
    inp_user()
    rock()
  elif human == "p":
    os.system("cls")
    inp_user()
    paper()
  elif human == "s":
    os.system("cls")
    inp_user()
    scissors()
    
  cpu = comp_move()
  if cpu == "rock":
    inp_comp()
    rock()
  elif cpu == "paper":
    inp_comp()
    paper()
  elif cpu == "scissors":
    inp_comp()
    scissors()

  if human == "r" and cpu == "scissors":
    hu = hu + 1
    co = co
  elif human == "r" and cpu == "paper":
    hu = hu
    co = co + 1
  elif human == "r" and cpu == "rock":
    hu = hu 
    co = co
  elif human == "p" and cpu == "scissors":
    hu = hu
    co = co + 1
  elif human == "p" and cpu == "paper":
    hu = hu
    co = co
  elif human == "p" and cpu == "rock":
    hu = hu + 1
    co = co
  elif human == "s" and cpu == "scissors":
    hu = hu
    co = co
  elif human == "s" and cpu == "paper":
    hu = hu + 1
    co = co
  elif human == "s" and cpu == "rock":
    hu = hu
    co = co + 1
 
  print(" ")
  print("You have got ",hu," win/s  and  computer has ",co," win/s")
  print(" ")
  Keep_going = input("Do you want to play again? ")
  Keep_going = Keep_going.lower()
  
os.system("cls")
print(" ")
if hu > co:
  print("You won!")
  print(" ")
elif hu < co:
  print("Computer won!")
  print(" ")
elif hu == co:
  print("It was a tie!")
  print(" ")
print("Hope you enjoyed playing. ")
