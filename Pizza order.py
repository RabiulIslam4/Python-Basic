print("Wellcome To Python Pizza Deliveries !")

size = input("What size pizza do you want? S, M or L ")
pepperoni = input("do you Want pepperoni? Y Or N ")
extra_cheese = input("do you want extra cheese? Y or N ")
bill = 0 
if size == "S" :
  bill += 15
elif size == "M" :
  bill += 20
elif size == "L" :
  bill += 25

if pepperoni == "Y" :
  if size == "S" :
    bill +=2
  else :
    bill += 3
if extra_cheese == "Y" :
  bill += 1           

print(f"Your Final Bill Is ${bill}")  
