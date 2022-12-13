import random
user = int(input("Enter Your Coin Side.'Head' for 0 or 'Tail' for 1.  "))
side = random.randint(0,1)

if side == user :
  print("You Win")
else :
  print("You Lose")  
