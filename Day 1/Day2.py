print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill? $"))
people = int(input("Hpw many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10,12, or 15?"))
total_tip = total_bill * (tip_percentage / 100)
total_bill_after_tip = total_bill + total_tip
per_person_bill = (total_bill_after_tip / people)

print(f"each person should pay {per_person_bill}")
