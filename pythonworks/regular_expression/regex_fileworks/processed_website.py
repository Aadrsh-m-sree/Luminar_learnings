from re import fullmatch,findall
f=open("C:\\Users\\adars\\OneDrive\\Desktop\\PySphere\\pythonworks\\regular_expression\\regex_fileworks\\website.txt")

content = f.read()
pattern = r"https?://[\w\S]+"

urls = findall(pattern,content)

for url in urls:
    print(url)
