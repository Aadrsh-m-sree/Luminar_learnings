# 1. Create a dictionary to store the names and ages of 5 people. Access and print the age of one person using their name.

people = {  'Alice' : 20,
            'Bob' : 24,
            'Charlie' : 35,
            'Dane' : 29,
            'Elisa' : 23
          }
print(people.get('Alice'))

# 2. Write a Python program to merge two dictionaries.

peoples1 = { 'Alice' : 20,
            'Bob' : 24,
            'Charlie' : 35,
            'Dane' : 29,
            'Elisa' : 23
          }

peoples2 = { 'Frank' : 40,
             'Grace' : 31,
             'Henry' : 27,
             'Isla' : 22,
             'Jack' : 26}

user_data = {**peoples1 , **peoples2 }
print(user_data)


# 3. Given a dictionary where the keys are student names and the values are their scores, write a program to calculate the average score.

students = { 'Alice' : 85,
             'Bob' : 78,
             'Charlie' : 92,
             'Dane' : 88,
             'Elisa' : 81,
             'Frank' : 75,
             'Grace' : 90,
             'Henry' : 83,
             'Isla' : 77,
             'Jack' : 80
           }

# count
# total 
# avg
marks = [mark for mark in students.values()]
count = len(marks)
total = sum(marks)
avg = total / count
print(avg)

# 4. Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers.

numbers = [1,2,3,4,5,6,7,8,9,10]
sqre = {number:number**2 for number in numbers}
print(sqre)

# 5. Write a Python program to create a dictionary from a list of keys and values using dictionary comprehension.

key_value_list = ['A','apple','B','banana','C','carrot','D','dragonfruit','K','Kiwi']

fruits_dict = {key_value_list[fruit]: key_value_list[fruit+1] for fruit in range(0,len(key_value_list),2)}
print(fruits_dict)

# 6. Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair them together into a dictionary.

fruits = ['Apple','Cherry','Orange','Kiwi','Grape','Watermelon']
prices = [180,300,80,460,220,50]

fruits_data = {fruit:price for fruit,price in zip(fruits,prices)}

print(fruits_data)

# 7. Write a Python program to filter a dictionary, keeping only items with values greater than 50 using dictionary comprehension.

fruit_dict = {  'Apple': 180, 
                'Cherry': 300,
                'Orange': 80, 
                'Kiwi': 460, 
                'Grape': 220, 
                'Watermelon': 50}

greater_than_fifty = {k:v for k,v in fruit_dict.items() if v>50}
print(greater_than_fifty)

# 8. Given a sentence, count the frequency of each word using a dictionary.

word = """The cat and the dog saw the cat and the dog with the cat 
           and the dog while the cat and the dog werechasing the cat and the dog"""
word_list = word.split()
frequency = { w:word_list.count(w) for w in word_list}
print(frequency)

# 9. Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.

num_list = [10,-20,4,-6,-8,2,1,9,-53,443]
abs_dict = {num:abs(num) for num in num_list}
print(abs_dict)


# 10. Given a dictionary of items and their prices, write a program to apply a 10% discount to all the items using dictionary comprehension.


fruit_dict = {  'Apple': 180, 
                'Cherry': 300,
                'Orange': 80, 
                'Kiwi': 460, 
                'Grape': 220, 
                'Watermelon': 50}

after_disc = {fruit:price // 10 * 9 for fruit,price in fruit_dict.items()}
print(after_disc)