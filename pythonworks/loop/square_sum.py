num = int(input('enter a number :'))
total = 0

while (num > 0):
    rem = num %10
    square = rem*rem
    total += square
    num = num // 10
print(total)