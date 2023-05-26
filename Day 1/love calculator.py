print("Welcome to love calculator")
name1 = input("Enter person 1 name")
name2 = input("Enter person 2 name")
lower_case_string = (name1 + name2).lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

true = t + r + u + e
love = l + o + v + e

print(f"Your love score is {true}{love}")
