import random
lists  = input("Give Everybody's Name, Separate By a Coma. ")

names = lists.split(",")

lenths = len(names)
random_names = random.randint(0, lenths - 1)
person = names[random_names]

print(person + " is Going To buy the meal today !")
