arr=[2,4,6,3,8,7]
search=int(input("Enter the element :"))
is_present=False
for i in range(len(arr)):
    if search==arr[i]:
        is_present=True
        break
print(f"The element {search} is found in index {i}" if is_present==True else "Not present")