print("Intersection")

st1 = {10,20,30,40,50}
st2 = {10,20,60,70,80}
inter_set = st1.intersection(st2)
print(inter_set)

print("............................")
print("Union")

st1 = {10,20,30,40,50}
st2 = {10,20,60,70,80}
union_set = st1.union(st2)
print(union_set)

print("............................")
print("Difference")

st1 = {10,20,30,40,50}
st2 = {10,20,60,70,80}
dif_set=  st1.difference(st2)
print(dif_set)

print("............................")
print("Remove")

st1 = {10,20,30,40,50}
st1.remove(20)
print(st1)

print("............................")
print("User suggestion")

users = ['Rahul','Rohit',"Kohli",'Rishabh','Pandya','Sanju','Siraj']
rahul_Following = ["Rohit","Kohli",'Rishabh','Rahul']
sanju_following = ['Sanju','Rohit','Kohli']

suggestion = set(users).difference(set(rahul_Following))
mutual_friends = set(rahul_Following).intersection(set(sanju_following))


print(suggestion)
print(mutual_friends) 

print("............................")
print("Subset")

st1 = {1,2,3}
st2 = {1,2,3,4,5}
print(st1.issubset(st2))

print("............................")
print('Superset')

st1 = {1,2,3}
st2 = {1,2,3,4,5}
print(st2.issuperset(st1))

print("............................")
print("Symmetric difference")


st1 = {1,2,3,10,20}
st2 = {1,2,3,4,5}
syd = st1.symmetric_difference(st2)
print(syd)

print("............................")
print("Update")

st1 = {1,2,3,10,20}
st2 = {1,2,3,4,5}

st1.update(st2)
print(st1)

print('Remove duplicates')
text = 'this is a test to remove duplicate words this test is simple'
my_lst = text.split()
my_st = set(my_lst)
print(my_st)

# words = text.split()
# print(set((words)))

print("............................")

text1 = 'this simple test remove duplicate words'
my_lst2 = text1.split()
my_st2 = set(my_lst2)
print(my_st2)

print(my_st2.issubset(my_st))
