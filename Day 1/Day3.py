height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight / height ** 2)
if (BMI < 18.5):
    print(f"They are underweight and bmi is {BMI}")
elif (BMI > 18.5 and BMI < 25):
    print(f"They are normal Weight and bmi is {BMI}")
elif (BMI > 25 and BMI < 30):
    print(f"They are overweight and bmi is {BMI}")
elif (BMI > 30 and BMI < 35):
    print(f"They are obese and bmi is {BMI}")
elif (BMI > 35):
    print(f"They are clinically obese and bmi is {BMI}")
else:
    print("unknown answer")
