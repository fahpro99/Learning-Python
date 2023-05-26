print("Welcome to treasure island !")
print("Your mission is to find the treasure.")

decision = input("Type left or right\n")

if (decision.lower() == "left"):
    decision2 = input("swim or wait\n")
    if (decision2.lower() == "wait"):
        decision3 = input("Which door Blue, Red, Yellow?\n")
        if (decision3.lower() == "yellow"):
            print("you Win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
