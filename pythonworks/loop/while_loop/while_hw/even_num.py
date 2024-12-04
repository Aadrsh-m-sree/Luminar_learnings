# 9. Print Even Numbers in a Range:
#    - Write a Python program to print all even numbers between 1 and 50 using a `while` loop.

limit = int(input("enter limit :"))
i = 1
while(i <= limit):
    if i%2 == 0:
        print(i)
    i += 1 
    
    