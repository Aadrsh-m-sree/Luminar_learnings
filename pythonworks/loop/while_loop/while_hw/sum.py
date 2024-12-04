# 10. Sum of Digits:
#     - Write a Python program to find the sum of the digits of a given number using a `while` loop.

number = int(input("enter number :"))
result = 0
while(number > 0):
    rem = number % 10
    result += rem
    number = number // 10
print(result)