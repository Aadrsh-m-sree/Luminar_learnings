num1 = int(input("enter 1st number :"))
num2 = int(input("enter 2nd number :"))

max_num = num1 if num1>num2 else num2
LCM = max_num
while(LCM % num1 != 0 or LCM % num2 != 0):
    LCM += LCM
print(LCM)






