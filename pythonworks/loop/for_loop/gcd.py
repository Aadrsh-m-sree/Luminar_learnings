# num1 = int(input("enter number 1 :"))
# num2 = int(input("enter number 2 :"))
# for i in range(1, num1+1):
#     if num1 % i == 0 and num2 %i ==0:
#          print(i)


# num1 = int(input("enter number 1 :"))
# num2 = int(input("enter number 2 :"))

# min_num = num1 if num1<num2 else num2
# gcd = 1
# for i in range(1, min_num+1):
#     if num1 % i == 0 and num2 %i ==0:
#        gcd = i
# print(gcd) 



num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))

min_num = min(num1,num2)
gcd = 1
for i in range(1, min_num+1):
    if num1 % i == 0 and num2 %i ==0:
       gcd = i
print(gcd) 