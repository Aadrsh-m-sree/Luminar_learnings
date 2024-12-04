f=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\question.txt")
words=[]
for line in f:
    line=line.rstrip("\n")
    all_words=line.split(" ")
    for w in all_words:
        words.append(w)
sorted_list=sorted(words,key=lambda w:words.count(w),reverse=True) 
word_freq={w:sorted_list.count(w) for w in sorted_list} 
most_frequent=max(word_freq,key=lambda w:word_freq.get(w))
print(sorted_list)  
print(word_freq)   
print(most_frequent)

# word_count={w:words.count(w) for w in words}
# nested_word_count=[[v,k] for k,v in word_count.items()]
# print(sorted(nested_word_count,reverse=True)[0])