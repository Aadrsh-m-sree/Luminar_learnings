fr=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\fruits.txt")

fruits=[]

for fruit in fr:
    fruits.append(fruit.rstrip("\n"))
print(fruits)