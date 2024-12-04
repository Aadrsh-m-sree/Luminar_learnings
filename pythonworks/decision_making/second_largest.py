Num1 = int(input(" enter num1 "))
Num2 = int(input(" enter num2 "))
Num3 = int(input(" enter num3 "))

# if Num1 > Num2 and Num1 < Num3:
#     print (f"{Num1} is the second largest")
# elif Num2 > Num1 and Num2 < Num3:
#     print (f"{Num2} is the second largest")
# else:
#     print (f"{Num3} is the largest")



if Num1 > Num2 and Num1 > Num3:
    if Num2> Num3:
        print(f"{Num2} is the second largest")
    else:
       print(f"{Num3} is the second largest")
elif Num2 > Num1 and Num2 > Num3:
    if Num1> Num3:
        print(f"{Num1} is the second largest")
    else:
       print(f"{Num3} is the second largest")
elif Num3 > Num1 and Num3 > Num2:
    if Num1> Num2:
        print(f"{Num1} is the second largest")
    else:
       print(f"{Num2} is the second largest")
elif Num1 == Num2 and Num1 == Num3:
   print('All numbers are equal')