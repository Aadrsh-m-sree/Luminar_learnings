# num1 = int(input("enter number 1 :"))
# num2 = int(input("enter number 2 :"))

# for num in range(0,num2):
#     if num2 != 0:
#         rem = num1% num2
#         num1 = num2
#         num2 =rem
# print("GCD =", num1)


num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))

min_num = min(num1,num2)
max_num = max(num1,num2)

for num in range(0,min_num):
    if min_num != 0:
        rem = max_num % min_num
        max_num = min_num
        min_num = rem
print("GCD =", max_num)