# 13. Find the Largest Digit:
#     - Write a Python program to find the largest digit in a given number using a `while` loop.

number = int(input("enter number :"))
largest = 0

while(number > 0):
    num = number % 10
    if num > largest:
        largest = num
    number = number // 10
print(largest)