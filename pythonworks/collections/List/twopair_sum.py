# arr=[2,3,4,5]
# find=False
# val=7
# for i in range(len(arr)-1):
#     first=arr[i]
#     for j in range(i+1,len(arr)):
#         if val==first+arr[j]:
#                find=True
#                print(first,arr[j])
#                break
#     if find==True:
#         break

arr=[2,3,5,4]
find=False
val=int(input("Enter the input :"))
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if val==arr[i]+arr[j]:
               find=True
               print(arr[i],arr[j])
               break
    if find==True:
        break
