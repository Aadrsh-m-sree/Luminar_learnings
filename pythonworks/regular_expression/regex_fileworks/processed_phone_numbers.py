from re import fullmatch
f = open("C:\\Users\\adars\\OneDrive\\Desktop\\PySphere\\pythonworks\\regular_expression\\regex_fileworks\\phone_numbers.txt")

for line in f:
    phone = line.rstrip("\n")

    pattern = r"(91)?[6-9][0-9]{9}"
    matcher = fullmatch(pattern,phone)

    if matcher != None:
        print(phone)