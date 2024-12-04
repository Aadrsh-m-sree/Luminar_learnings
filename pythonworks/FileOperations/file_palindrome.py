fread=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\words.txt","r")
f_palindrome=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\palindrome.txt","w")

for word in fread:
    word=word.rstrip("\n")
    if word==word[::-1]:
        print(word)
        f_palindrome.write(word+"\n")
fread.close()
f_palindrome.close()