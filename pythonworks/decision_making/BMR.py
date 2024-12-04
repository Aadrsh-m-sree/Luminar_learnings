weight = int(input("enter weight in kg :"))
height = int(input("enter height in cm :"))
age = int(input("enter age :"))
gender = input(" Gender [ Male : M ] [ Female : F ] ").upper()

if gender == 'M':
# BMR (kcal/day) = 10 × weight (kg) + 6.25 × height (cm) – 5 × age (y) + 5 (kcal/day)
    BMR = 10 * weight + 6.25 * height - 5 * age + 5
    print(f"your BMR is {round(BMR)}")
elif gender == 'F':
# BMR (kcal/day)= 10 × weight (kg) + 6.25 × height (cm) – 5 × age (y) – 161 (kcal/day)
    BMR = 10 * weight + 6.25 * height - 5 + age - 161
    print(f"your BMR is {round(BMR)}")
else:
    print("Enter a valid gender ☺")

activity_level = int(input(
    """Select activity level

    1 : Sedentary
    2 : Lightly active
    3 : Moderately active
    4 : Very active
    5 : Extra active
    """ ))
if activity_level == 1:
    TDEE = BMR * 1.2
    print(f"TDEE = {round(BMR * 1.2)}")
elif activity_level == 2:
    TDEE = BMR * 1.375
    print(f"TDEE = {round(BMR * 1.375)}")
elif activity_level == 3:
    TDEE = BMR * 1.55
    print(f"TDEE = {round(BMR * 1.55)}")
elif activity_level == 4:
    TDEE = BMR * 1.725
    print(f"TDEE = {round(BMR * 1.725)}")
elif activity_level == 5:
    TDEE = BMR * 1.9
    print(f"TDEE = {round(BMR * 1.9)}")


target_weight = int(input("enter weight to reduce in kg :"))
duration = int(input("enter duration in weeks :"))
calorie_deficit = target_weight * 7700
days = duration  * 7
daily_calorie_deficit = calorie_deficit / days

print(f"""To reduce {target_weight} kg in {duration} weeks
    reduce your TDEE from {TDEE} to {TDEE-daily_calorie_deficit}
    Current TDEE = {TDEE}
    Deficit in a day = {daily_calorie_deficit}
    Difference = {TDEE-daily_calorie_deficit}

""")


