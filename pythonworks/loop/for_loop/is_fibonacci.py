prev = 0
current = 1
num = int(input("enter number"))
next = prev + current
is_fib= False
while(next <= num):
    if next == num:
        is_fib == True
        break
    next = prev+current
    prev,current = current,next
print(is_fib)


is_fibonacci = False
first = 0
second = 1
fib = 0
num = int(input("enter num :"))
i = 0
while(i <= num):
    if first + second == num :
        is_fibonacci = True
        break
    fib = first+second
    first = second
    second = fib
    i+=1
print(is_fibonacci)



is_fibonacci = False
first = 0
second = 1
num = int(input("enter num :"))

if num == first  or num == second:
    is_fibonacci = True
    print(is_fibonacci)
else:
    while second < num:
        fib = first + second
        if fib == num:
            is_fibonacci = True
            break
        first = second
        second = fib
print(is_fibonacci)










