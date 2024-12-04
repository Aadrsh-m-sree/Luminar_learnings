from re import fullmatch

# lowercase
# starts with an alphabet
# numbers optional
# @gmail.com
# before @ 6-64 charachters


email_id = input("enter email id :")
pattern = "[a-z]+[a-z0-9]{5,63}@gmail.com"
matcher = fullmatch(pattern,email_id)
if matcher == None:
    print("Invalid")
else:
    print("Valid")