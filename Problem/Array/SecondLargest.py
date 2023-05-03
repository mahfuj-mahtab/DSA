# solution in Bubble Sort
arr = [int(x) for x in input().strip().split()]

for i in range(len(arr)):
    for j in range(0,len(arr)-1):
        if(arr[i] < arr[j]):
            arr[j],arr[i] = arr[i],arr[j]


c = 0
small = 0
for i in range(len(arr)-1,-1,-1):
    if(arr[-1] > arr[i]):
        c+=1
        small = arr[i]
        break
if(c == 0):
    print(-1)
else:
    print(small)