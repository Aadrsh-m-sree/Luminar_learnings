# # # palindrome  
word = input("enter word :")
word_lst = list(word)
print(word_lst)
reverse_word = word_lst[::-1]
print(reverse_word)

if word_lst == reverse_word:
    print("palindrome")
else:
    print("not palindrome")


# longest_sublist
lst= [[1,2],
      [1,2,3,4,[5,6,7],8],
      [9,10,11,[12,13],[14,15],16,[17,18]],
      [19,[20,21],[22,23],[24,25],26,[27,28,29,30,31,32,33,34]]
      ]

longest_sublist = []
max_length = 0
for i in lst:
    current_length = len(i)
    if current_length > max_length:
        max_length = current_length
        longest_sublist = i 
print(longest_sublist)

# most recursive
text= "this is a simple python program that print most recursive word. this program is simple"
word = text.split()
most_recursive = {x:word.count(x) for x in word}
wordd = max(most_recursive.items(),key=len)
print(wordd)

# text with maximum charachter
text = "this is a simple question return word with maximum number of characters"
word = text.split()
max_word = max(word, key=len)
print(max_word)

