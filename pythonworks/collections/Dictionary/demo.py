# print("create dictionary \n")
# # create a dictionary products with id,title,price,brand

# products = {'id':10,'title':'Car','price':20000000,'brand':'McLaren'}
# print(products)
# print(products['price'])

# print("............................................")
# print("update\n")

# products['price']= 5000000
# print(products)

# print("............................................")
# print('add \n')

# products['torque'] = '1200N'
# print(products)

# print("............................................")
# print('add key with condition \n')
# # add offer as 10 if offer exists else 20

# if 'offer' in products:
#     products['offer'] = 10
# else:
#     products['offer'] = 20

# print(products)
# print("............................................")


# print("new dict employee \n")

# employee = {"E.Id":12,
#             'Name':'John',
#             'Salary':150000,
#             'Department':'HR',
#             'Experience':4
#             }

# print(employee)
# print(employee['Salary'])
# print("............................................")
# print('update \n')

# employee['contact']= 9023902390
# print(employee)

# print("............................................")
# print('update \n')

# """if experience > 5 update employee salary as current salary+10000
# else current salary + 5000"""

# if employee['Experience'] > 5:
#     employee['Salary'] += 40000
# else:
#     employee['Salary'] += 20000

# print(employee)

# print("............................................")
# print('update \n')

# if employee['Experience'] > 5:
#     employee['Role'] = 'SDE'
# else:
#     employee['Role'] = 'JDE'

# print(employee)

# print("............................................")

# print('word count \n')

# word = ['hai','hello','hai','hello','hai']

# word_count = {}

# for w in word:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)

# print("............................................")


# orders = ['tea','coffee','tea','coffee','gheeroast','plainroast','porotta','tea']
# # order_summary = {}

# # for item in orders:
# #     if item in order_summary:
# #         order_summary[item]+=1
# #     else:
# #         order_summary[item]=1
# # print(order_summary)

# order_summ = {o:orders.count(o) for o in orders} #NOTE - # dictionary comprehenstion
# print(order_summ)

# print("............................................")

# text = 'ABBACB'

# # for ch in text:
# #     print(ch)

# char_count = {ch:text.count(ch) for ch in text}
# print(char_count)

print("*******************************************")
# 26/09/2024

print('get() \n')

Employee = {'Id':109,'Name':'Mark','Department':'Resource Management','Age':34,'Salary':52000}
print(Employee.get('Salary'))

print("............................................")
print('pop() \n')

Employee.pop('Salary')
print(Employee)

print("............................................")
print('keys() \n')

for k in Employee.keys():
    print(k)

print("............................................")
print('values() \n')

for v in Employee.values():
    print(v)

print("............................................")
print('items() \n')

for k,v in Employee.items():
    print(k,v)

print("............................................")
print('dictionary comprehension')


arr = [10,20,30,40,2,3]

s={}
for i in arr:
    square = i**2
    s[i]=square
print(s)
print()

# my_dict = {x:x*x for x in arr}
# print(my_dict)


arr = [10,20,30,40,2,3,7,8,9]
even_square = {num : num * 2 for num in arr if num % 2 == 0}
print(even_square)
print()
odd_qube = {num : num**2 for num in arr if num % 2 != 0}
print(odd_qube)

print("............................................")
print('frequency count')

arr = [10,20,30,40,2,3,7,8,9,10,30]
freq_count={num:arr.count(num) for num in arr}
print(freq_count)
print()

print('recursive')
text = 'ABABBCCDDE'
char_occurance = {char:text.count(char) for char in text}
print(char_occurance)
print()

print('non recursive')
text = 'ABABBCCDDE'
char_occurance = {char:text.count(char) for char in text if text.count(char) == 1}
print(char_occurance)

non_recursive = [k for k,v in char_occurance.items() if v == 1]
print(non_recursive)

for k,v in char_occurance.items():
    if  v == 1:
        print(k)


print('recursive words')
words = ['hello','hai','hello','this','is','this','is','hello']
word_frequency = {w:words.count(w) for w in words}
print(word_frequency)
print()
recursive = [k for k,v in word_frequency.items() if v>1]
print(recursive)
print()
non_recursive = [k for k,v in word_frequency.items() if v == 1]
print(non_recursive)
print()



