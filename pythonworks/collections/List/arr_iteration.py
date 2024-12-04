# arr = [10,20,30,40,50]
# for i in range(0,len(arr)):
#     print(arr[i])


# arr = [1,2,3,4,5,6,7,8,9,10]
#print even numers

# for i in arr:
#     if i%2==0:
#         print(i)

# for i in range(0,len(arr)):
#     if arr[i]%2==0:
#         print(arr[i])


arr= [1,2,3,4,5,6,7,8,9]
sum = 7
for i in range(0,len(arr)):
    # j = i+1
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == sum:
            print(arr[i],arr[j])
            break
        

# arr= [2,3,4,5]
# sum = int(input("enter sum"))

# for i in range(0,len(arr)-1):
#     for j in range(i+1,len(arr)):
#         current_sum = arr[i]+arr[j]

#         if sum == current_sum:
#             print(arr[i],arr[j])

#             break



lst = [2,3,4,5]
# output = 12 , 11 , 10 , 9


for i in range(0,len(lst)):
    op = sum(lst) - lst[i]
    print(op)
