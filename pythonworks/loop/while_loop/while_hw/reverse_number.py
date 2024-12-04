# 4. Reverse a Number:
#    - Write a Python program to reverse a given number using a `while` loop.


number = int(input('enter a number :'))
reversed_num = 0

while(number > 0):
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10

print(reversed_num)
