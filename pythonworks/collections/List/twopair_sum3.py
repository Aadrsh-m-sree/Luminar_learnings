arr=[2,3,4,5,6,7,8,9]
val=int(input("Enter the value :"))
count=0
left=0
right=len(arr)-1
if(val>sum(arr)):
    print("error")
else:
    while(left<right):
        curr_sum=arr[left]+arr[right]
        if curr_sum==val:
            print(arr[left],arr[right])
            break
        elif curr_sum>val:
            right-=1
        elif curr_sum<val:
            left+=1
        count+=1
print(count)