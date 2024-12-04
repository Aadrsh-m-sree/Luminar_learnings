# validate pancard

# 3 alphabets
# 1 alphabet (PCAFHT)
# 1 alphabet
# 4 numbers
# 1 alphabet

from re import fullmatch

Pancard_number = input("enter pancard number :")
pattern = "[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"
matcher = fullmatch(pattern,Pancard_number)
if matcher == None:
    print("Invalid")
else:
    print("Valid")

