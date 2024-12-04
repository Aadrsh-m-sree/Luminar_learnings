arr=[100,200,300,400,500]
k=int(input("Enter the number of rotations:"))
for i in range(1,k+1):
    poped=arr.pop()
    arr.insert(0,poped)
    print(f"rotation {i}")
    print(arr)
    