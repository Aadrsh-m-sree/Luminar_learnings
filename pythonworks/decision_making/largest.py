Num1 = int(input("enter num1 "))
Num2 = int(input("enter num2 "))
Num3 = int(input(" enter num3 "
                 ))
if Num1 > Num2 and Num1 > Num3:
   print (f"{Num1} is the biggest")

elif Num2 > Num1 and Num2 > Num3:
   print (f"{Num2} is the biggest") 

elif Num3 > Num1 and Num3 > Num2:
   print (f"{Num3} is the bigges")
   
elif Num1 == Num2 and Num1 == Num3:
   print('All numbers are equal')