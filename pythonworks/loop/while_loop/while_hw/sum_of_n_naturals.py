# 2. Sum of First N Natural Numbers:
#  - Write a Python program to calculate the sum of the first N natural numbers using a `while` loop.

n = int(input("enter count on natural numbers :"))

sum = 0
i = 1

while(i <= n):
    sum += i
    i+=1
print(sum)