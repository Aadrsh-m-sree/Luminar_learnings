arr=[1,2,2,2,1,4,5]
arr.sort()
duplicate=[]
print(arr)
for i in range(0,len(arr)-1):
    j=i+1
    sub=arr[j]-arr[i]
    print(sub)
    if sub==0:
        if arr[i] not in duplicate:
            duplicate.append(arr[i])
print(duplicate)