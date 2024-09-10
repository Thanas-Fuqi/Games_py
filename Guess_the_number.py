
import random
Num = random.randint(1 ,10)
score = 100

Nim = input("What number do you think I am? ")
Nim = int(Nim)

if Nim != Num:
  if Num%2 == 1:
    print("I am an odd number")
    score = score - 25
    print("You have ",score," Points")
    Nim = input("What number do you think I am? ")
    Nim = int(Nim)
    if Nim != Num: 
      if Num >= 5 and Num <= 10:
        print("I am between 5 and 10")
        score = score - 25
        print("You have ",score," Points")
        Nim = input("What number do you think I am? ")
        Nim = int(Nim)
        if Nim == Num:
          print("You have found me")
          print("You have won with ",score," Points")
        else:
          print("You loosed and I am ",Num)
          print("You have lost with 0 Points")
      elif Num >= 0 and Num <= 5:
        print("I am between 0 and 5")
        score = score - 25
        print("You have ",score," Points")
        Nim = input("What number do you think I am? ")
        Nim = int(Nim)
        if Nim == Num:
          print("You have found me")
          print("You have won with ",score," Points")
        else:
          print("You loosed and I am ",Num)
          print("You have lost with 0 Points")
    else:
      print("You have found me")
      print("You have won with ",score," Points")
        
  elif Num%2 == 0:
    print("I am an even number")
    score = score - 25
    print("You have ",score," Points")
    Nim = input("What number do you think I am? ")
    Nim = int(Nim)
    if Nim != Num: 
      if Num >= 5 and Num <= 10:
        print("I am between 5 and 10")
        score = score - 25
        print("You have ",score," Points")
        Nim = input("What number do you think I am? ")
        Nim = int(Nim)
        if Nim == Num:
          print("You have found me")
          print("You have won with ",score," Points")
        else:
          print("You loosed and I am ",Num)
          print("You have lost with 0 Points")
      elif Num >= 0 and Num <= 5:
        print("I am between 0 and 5")
        score = score - 25
        print("You have ",score," Points")
        Nim = input("What number do you think I am? ")
        Nim = int(Nim)
        if Nim == Num:
          print("You have found me")
          print("You have won with ",score," Points")
        else:
          print("You loosed and I am ",Num)
          print("You have lost with 0 Points")
    else:
      print("You have found me")
      print("You have won with ",score," Points")
        
else:
  print("You have found me")
  print("You have won with ",score," Points")
