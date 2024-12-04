arr=[3,4,2,1,1,6,4,1,3]
for i in range(len(arr)-2):
    v1=arr[i]
    v2=arr[i+1]
    v3=arr[i+2]
    if v1<v2>v3:
        print("peak=>",v1,v2,v3)
    elif v1>v2<v3:
        print("Valley=>",v1,v2,v3)