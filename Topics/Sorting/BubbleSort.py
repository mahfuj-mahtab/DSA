arr = [int(x) for x in input().strip().split()]

for i in range(len(arr)):
    for j in range(0,len(arr)-1):
        if(arr[i] < arr[j]):
            arr[j],arr[i] = arr[i],arr[j]
    
print(arr)