lst1 = ['apple' , 'mango' ,'onion' ,'potato']
lst2 = [100,200]
balance_indices = [i-1 for i in range(len(lst2), len(lst1))]

new_dict = {x:y for x,y in zip(lst1,lst2+balance_indices)}
print(new_dict)

result = {}
for i in range(0,len(lst2)):
    lst1_index_elem = lst1[i]
    lst2_index_elem = lst2[i]
    result[lst1_index_elem] = lst2_index_elem
print(result)

balance = lst1[len(lst2):]

for index, elements in enumerate(balance):
    result[elements] = index-1
print(result)


