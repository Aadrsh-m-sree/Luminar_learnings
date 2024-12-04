# arr1=[10,13,8,11,20]
# len1=len(arr1)
# arr2=[2,20,8,7,13]
# len2=len(arr2)
# l=0
# for i in range(len1):
#     l+=1
#     for j in range(len2):
#         l+=1
#         if arr1[i]==arr2[j]:
#             print(arr1[i],end=" ")
# print(l)

# arr1=[10,13,8,11,20]
# # arr1=[2,20,8,7,13]
# arr1.sort() # [8,10,11,13,20]
# arr2=[2,20,8,7,13]
# # arr2=[10,13,8,11,20]
# arr2.sort() # [2,7,8,13,20]
# l=0
# for i in range(len(arr1)):
#     l+=1
#     for j in range(len(arr2)):
#         l+=1
#         if arr1[i]==arr2[j]:
#             print(arr1[i])
#         elif arr2[j]>arr1[i]:
#             break
# print(l)



arr1=[10,13,8,11,20]
arr1.sort() # [8,10,11,13,20]
arr2=[2,20,8,7,13]
arr2.sort() # [2,7,8,13,20]
l=0
p1=0
p2=0
while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(arr1[p1])
        p1+=1
        p2+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
    