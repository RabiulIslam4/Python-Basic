player = input("Do You Want To Enter The Quiz? ").lower()
if player != "yes" :
  quit()
print("Okay Lets Start The Quiz !")

score = 0
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit" :
  print("Correct !")
  score += 1
else :
 print("Incorrect")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit" :
  print("Correct !")
  score += 1
else :
  print("Incorrect")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory" :
  print("Correct !")
  score += 1
else :
  print("Incorrect")

answer = input("What does SOC stand for? ").lower()
if answer == "security operation center" :
  print("Correct !")
  score += 1
else :
  print("Incorrect")

answer = input("Which is the first search engine in Internet? ").lower()
if answer == "archie" :
  print("Correct !")
  score += 1
else :
  print("Incorrect")

answer = input("First computer virus is known as? ").lower()
if answer == "creeper virus" :
  print("Correct !")
  score += 1
else :
  print("Incorrect")

answer = input("Firewall in computer is used for? ").lower()
if answer == "security" :
  print("Correct !")
  score += 1
else :
  print("Incorrect")
print("Your Score is " + str(score) + ".")
print("You got " + str(int(score/7 * 100)) + "%.")
