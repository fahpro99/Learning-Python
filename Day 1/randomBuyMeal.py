import random

myStr = input("Gimme a list of name \n")
people = myStr.split(",")

randomChoice = random.randint(0, len(people) - 1)
print(f"{people[randomChoice]} is going to buy meal for me")
