# 7. Count the Number of Digits:
#    - Write a Python program to count the number of digits in a given number using a `while` loop.

number = int(input())
count = 0

while(number > 0):
    number = number // 10
    count+=1

print(count)
