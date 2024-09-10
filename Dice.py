
import random

def win():
  if ran == 1:
    print("  ------------    ")
    print(" |            |   ")
    print(" |      0     |   ")
    print(" |            |   ")
    print("  ------------    ")

  elif ran == 2:
    print("  ------------    ")
    print(" |  0         |   ")
    print(" |            |   ")
    print(" |         0  |   ")
    print("  ------------    ")

  elif ran == 3:
    print("  ------------    ")
    print(" | 0          |   ")
    print(" |      0     |   ")
    print(" |          0 |   ")
    print("  ------------    ") 

  elif ran == 4:
    print("  ------------    ")
    print(" |  0       0 |   ")
    print(" |            |   ")
    print(" |  0       0 |   ")
    print("  ------------    ")

  elif ran == 5:
    print("  ------------    ")
    print(" | 0        0 |   ")
    print(" |      0     |   ")
    print(" | 0        0 |   ")
    print("  ------------    ")

  elif ran == 6:
    print("  ------------    ")
    print(" | 0        0 |   ")
    print(" | 0        0 |   ")
    print(" | 0        0 |   ")
    print("  ------------    ")
   
Ok = input("To roll the dice press R ")
Ok = Ok.lower()

if Ok == "r":
  ran = random.randint(1, 6)
  win()
  print("\n")
  but = input("Do you want to roll again? ")
  but = but.lower()
  
  while but == "yes":
    print("\n")
    ran = random.randint(1, 6)
    win()
    but = input("Do you want to roll again? ")
    but = but.lower()
   