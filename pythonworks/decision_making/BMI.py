# progremme to calculate BMI

# BMI = weight in kg / (height in mtr) **2
weight_in_kg = int(input("enter your weight in Kilograms :"))
height_in_cm = int(input("enter your weight in centimeters :"))
height_in_mtrs = height_in_cm / 100

BMI = weight_in_kg / (height_in_mtrs) ** 2

if BMI < 16 :
    print(f"Your BMI is {BMI} and its Severe Thinness")
elif BMI >= 16 and BMI < 17:
    print(f"Your BMI is {BMI} and its Moderate Thinness")
elif BMI >= 17 and BMI < 18.5:
    print(f"Your BMI is {BMI} and its Mild Thinness")
elif BMI >= 18 and BMI < 25:
    print(f"Your BMI is {BMI} and its Normal")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI} and its Overweight")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI} and its Obese class I")
elif BMI >= 35 and BMI < 40:
    print(f"Your BMI is {BMI} and its Obese class II")
else :
    print(f"Your BMI is {BMI} and its Obese class III")



