Num1 = int(input(" enter num1 "))
Num2 = int(input(" enter num2 "))
Num3 = int(input(" enter num3 "))



if Num1 > Num2 and Num1 > Num3:

    if Num2> Num3:
        print(Num1, Num2 , Num3)
    else:
       print(Num1, Num3, Num2)

elif Num2 > Num1 and Num2 > Num3:

    if Num1> Num3:
        print(Num2 , Num1 , Num3)
    else:
       print(Num2 , Num3 , Num1)

elif Num3 > Num1 and Num3 > Num2:

    if Num1> Num2:
        print(Num3 , Num1 , Num2)
    else:
       print(Num3 , Num2 ,Num1)
       
elif Num1 == Num2 and Num1 == Num3:
   print('All numbers are equal')