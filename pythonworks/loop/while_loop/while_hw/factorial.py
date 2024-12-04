# 3. Factorial Calculation:
#    - Write a Python program to calculate the factorial of a given number using a `while` loop.

n = int(input("enter base number :"))

factorial = 1

while(n >= 1):
    factorial *= n
    n -=1
print(factorial)