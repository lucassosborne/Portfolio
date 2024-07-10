print("I'm thinking of a number between 1 & 10.")

import random

number = random.randint(1, 10)

while True:

  guess = int(input("Take a guess: "))
  
  if guess == number:
    print("You got it!")
    break
  elif guess < number:
    print("Higher")
  elif guess > number:
    print("Lower")