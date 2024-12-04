# 15. Print Multiplication Table:
#     - Write a Python program to print the multiplication table of a given number using a `while` loop.

num = int(input("enter a number :"))
limit =int(input("enter limit of multiplication table :"))
i=1
while(i<=limit):
    result = i*num
    print(f"{i} X {num} = {result}")
    i +=1