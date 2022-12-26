import string
import random

def generate_password(length):

  characters = string.ascii_letters + string.digits + string.punctuation

  #random.shuffle(characters)

  password = ''.join(random.sample(characters, length))
  return password

print(generate_password(8)) # prints a 8 character long password
print(generate_password(12)) # prints a 12 character long password
