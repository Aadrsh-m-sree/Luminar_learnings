# 6. Fibonacci Series:
#    - Write a Python program to print the Fibonacci series up to a specified number using a `while` loop.

limit = int(input("enter a limit :"))
first = 0
second = 1
i = 2

print(first,second ,end=" ")
while(i<=limit):
    fibonacci = first+second
    first = second
    second = fibonacci
    i+=1
    print(fibonacci , end= " ")

