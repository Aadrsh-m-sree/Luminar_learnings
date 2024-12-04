from re import findall
f=open("C:\\Users\\adars\\OneDrive\\Desktop\\PySphere\\pythonworks\\regular_expression\\regex_fileworks\\data.txt")
content = f.read()
# "(1|2)?[0-9]3[0-1]{1,2}/[0-9][12][0-2]{1,2}/(200|201)[0-9]{4}"
pattern = "[0-9]{2}/[0-9]{2}/[0-9]{4}"
date = findall(pattern,content)
for d in date:
    print(d)