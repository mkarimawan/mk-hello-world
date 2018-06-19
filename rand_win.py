import random


num = random.randint(1,10)

guess = int(input("Guess a number b/w 1 and 10:"))

while guess!=num:
    guess = int(input('Guess again:'))

print("You Win")
