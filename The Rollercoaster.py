print("Wellcome To The Rollercoaster !")

height = int(input("What Is Your Height in cm? "))
bill = 0
if height >= 120 :
  print("You Can Buy Roleercpaster Ticket.")
  age = int(input("What Is Your Age? "))
  if age <= 12 :
    bill = 5
    print("Child Tickets are $5")
  elif age <= 18 :
    bill = 7
    print("Youth Tickets Are $7")
  else :
    bill = 12
    print("Adult Tickets Are $12")
  want_photos = input("Do You Want A Photo Taken? Y or N ")   
  if want_photos == "Y" :
    bill = bill + 3
  print(f"Your Total Bill Is {bill}")    
else :
  print ("Sorry ! Your Can't Buy Rollercoaster Tickets.")
