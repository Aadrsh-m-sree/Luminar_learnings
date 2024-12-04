# progremme to calculate BMI

# BMI = weight in kg / (height in mtr) **2
weight_in_kg = int(input("enter your weight in Kilograms :"))
height_in_cm = int(input("enter your weight in centimeters :"))
height_in_mtrs = height_in_cm / 100

BMI = weight_in_kg / (height_in_mtrs) ** 2

print(f" your BMI is {round(BMI,1)}")