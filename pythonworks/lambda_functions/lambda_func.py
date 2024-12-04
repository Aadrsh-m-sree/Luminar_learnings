# lambda arguments: expression


# lambda for adding two numbers

add = lambda n1,n2 : n1+n2
print(add(10,20))


# subtraction

sub = lambda n1,n2 : n1 - n2
print(sub(20,30))


# cube

cube = lambda n1 : n1 **3 
print(cube(3))

# string length max

max_two = lambda str1,str2: str1 if len(str1) > len(str2) else str2
print(max_two('hai','hello'))

#string length min

min_two = lambda str1,str2: str1 if len(str1) < len(str2) else str2

print(min_two('hai','hello'))

# sub small from largest

smart_sub = lambda num1,num2 : num1-num2 if num1>num2 else num2-num1
print(smart_sub(20,100))

# max length

words = ['hai','hello','good','morning']
def get_length (word):
    return len(word)
print(max(words,key=get_length))

max_len = lambda word:len(word)
print(max(words,key=max_len))

# max_word_string


text = 'this is  a simple programming question to find word with maximum number of charachters'
words = text.split()
# def get_length(w):
#     return len(w)
# print(max(words,key=get_length))

max_len = lambda word:len(word)
print(max(words,key=max_len))


# sort

text = 'this is a simple programming question to find word with maximum number of charachters'
words = text.split()
def get_length(w):
    return len(w)
srtd_words = sorted(words,key=get_length,reverse=True)
print(srtd_words)

# # most recursive

text = 'this is is a simple programming question to find word with maximum number of charachters'

words = text.split()

def get_count(w):
    return words.count(w)

frequent_word = max(words,key=get_count)
print({frequent_word:words.count(frequent_word)})

text = 'ABAABBC'
# most recursive
# non recursive

def get_count(w):
    return text.count(w)
most_recursive = max(text,key=get_count)
print(most_recursive)


def get_count(w):
    return text.count(w)
non_recursive = min(text,key=get_count)
print(non_recursive)




