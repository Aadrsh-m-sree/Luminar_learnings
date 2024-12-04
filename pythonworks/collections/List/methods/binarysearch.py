arr=[5,3,2,6,1,8,7]
arr.sort()
print(arr)
search_element=int(input("Enter the element to be search :"))
is_present=False
low=0
upp=len(arr)-1

while(low<=upp):
    mid=(low+upp)//2
    if search_element==arr[mid]:
        is_present=True
        break
    elif search_element<arr[mid]:
        upp=mid-1
    elif search_element>arr[mid]:
        low=mid+1
print(f"Element is present at index {mid}" if is_present==True else "Not found")   
