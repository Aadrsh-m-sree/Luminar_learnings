# validate month

from re import fullmatch

Month = input("enter month :")

pattern = "([1-9]|0[1-9]|1[0-2])"

matcher = fullmatch(pattern,Month)

if matcher == None:
    print('Invalid')
else:
    print("Valid")