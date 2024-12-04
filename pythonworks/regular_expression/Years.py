from re import fullmatch

year = input("enter year")

# pattern = "(1[8-9]{1}[0-9]{2}|2[0][0-2][0-4])"

pattern = "((18|19)[0-9]{2}|(200|201)[0-9]{1}|202[0-4]{1})"

matcher = fullmatch(pattern,year)

if matcher == None:
    print("Invalid")
else:
    print("Valid")