# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[Jisan]
# *******************************************************************************''')

print("Wellcome To Treasure Island.")
print("Your Mission Is to Find The Treasure.")

cross_road = input("you're at a cross road. Where to You want To go? Type 'left' or 'right'")
case_cross_road = cross_road.lower()

if case_cross_road == "left" :
  lake = input('''You came To A Lake. There Is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.''')
  case_lake = lake.lower()
  if case_lake == "wait" :
    doors = input("you aarive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which colour do you choose?")
    case_doors = doors.lower()
    if case_doors == "red" :
      print("Game Over! Try Again")
    elif case_doors == "yellow" :
      print("Congratulations! You Found The Treasure.")
    else :
      print("Game Over! Try Again")   


  else :
    print("Game Over! Try Again")  


else :
  print("Game Over! Try Again")
