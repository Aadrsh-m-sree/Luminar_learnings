weight = int(input("enter weight in kg :"))
height = int(input("enter height in cm :"))
age = int(input("enter age :"))
gender = input(" Gender [ Male : M ] [ Female : F ] ").upper()

if gender == 'M':
# BMR (kcal/day) = 10 × weight (kg) + 6.25 × height (cm) – 5 × age (y) + 5 (kcal/day)
    BMR = 10 * weight + 6.25 * height - 5 * age + 5
   
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
elif activity_level == 2:
    TDEE = BMR * 1.375
elif activity_level == 3:
    TDEE = BMR * 1.55
elif activity_level == 4:
    TDEE = BMR * 1.725
elif activity_level == 5:
    TDEE = BMR * 1.9

response = int(input("""
                Are you planning to have balanced diet ?
                1 : If like to continue.
                2 : Will try later
                """))

if response == 1:
    plan = int(input("""
            1 : I want to gain weight
            2 : I want to lose weight
                        """))
    if plan == 1:
        Weight_Gain = int(input("How much do you want to gain"))
        
        time = int(input("select preferred time period"))
        
        Total_Weeks = time * 4
        Weekly_Weight_Gain = Weight_Gain / Total_Weeks 
        Weekly_Caloric_Surplus = 7700*Weekly_Weight_Gain
        Daily_Caloric_Surplus  = Weekly_Caloric_Surplus / 7
        Daily_Calories_for_Weight_Gain = TDEE  + Daily_Caloric_Surplus

        print(f""" if you need to gain {Weight_Gain} KG [{weight} to {weight + Weight_Gain}] in {time} weeks, 
            
            you should intake {round(Daily_Calories_for_Weight_Gain)} more calories in a day
            TDEE = {TDEE}
            More to gain = {round(Daily_Calories_for_Weight_Gain)}
            Additional calories in a day = {round(Daily_Calories_for_Weight_Gain) - round(TDEE)}

            """)

    elif plan == 2:
        lose = int(input("""How much do you want to lose
                        1 : 1 - 2 kilogram
                        2 : 2 - 5 kilogram
                        3 : 5 - 10 kilogram
                        """))
        time = int(input("""select preferred time period
                         
                        1 : 1 - 2 months
                        2 : 2 - 5 months
                        3 : 5 -9 months
                        """))
elif response == 2:
    print(f"""
        your BMR is {round(BMR)}
        your TDEE is {TDEE}
        Thank You for your response, stay Healthy
        """)


    