#Print the array in reverse order (without using reverse function).
#unstable one

arr = [1,2,6,8,10,23,14,11,70,88]

arr2=[]

for i in range(len(arr)):
    idx = len(arr)-i-1
    arr2.append(arr[idx])

print(arr2)
