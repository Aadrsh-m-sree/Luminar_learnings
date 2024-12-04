# 5. Check for Palindrome:
#    - Write a Python program that checks if a given number is a palindrome using a `while` loop.

number = int(input('enter a number :'))
original_number = number
reversed_num = 0

while(number > 0):
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10

if original_number == reversed_num:
    print(" number is a palindrome ")


word = input("enter word :")

