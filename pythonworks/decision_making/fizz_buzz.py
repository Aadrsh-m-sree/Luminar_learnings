num = int(input("enter a number :"))

if num % 15 == 0:
    print("fizzBuzz")
elif num % 5 == 0:
    print("buzz")
elif num % 3 == 0:
    print("fizz")
else:
    print("Invalid number")