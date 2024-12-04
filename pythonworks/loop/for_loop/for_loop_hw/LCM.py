# num1 = int(input("enter num1 :"))
# num2 = int(input("enter num2 :"))

# max_num = num1 if num1 > num2 else num2
# LCM = max_num
# for i in range(0, max_num):
#     if (LCM % num1 != 0 or LCM % num2 != 0):
#         LCM += max_num
# print(LCM)

num1 = int(input("enter num1 :"))
num2 = int(input("enter num2 :"))

max_num = max(num1,num2)
for i in range(max_num,(num1*num2)+1,max_num):
    if i % num1 == 0 and i % num2 == 0:
        print(i)
        break