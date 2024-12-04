from re import fullmatch,finditer
f=open("C:\\Users\\adars\\OneDrive\\Desktop\\PySphere\\pythonworks\\regular_expression\\regex_fileworks\\hashtag.txt")
content = f.read()
words = content.split()

for word in words:
    pattern = r"[#]\w+"
    match = fullmatch(pattern,word)
    if match != None:
        print(word)


for line in f:
    words = line.rstrip("\n")
    pattern = r"#\w+"
    matcher = finditer(pattern,words)
    for obj in matcher:
        print(obj.group())

    
