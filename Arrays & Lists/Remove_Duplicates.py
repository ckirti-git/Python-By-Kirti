#Remove duplicates from the array and print the unique elements.

arr = [1,2,4,1,2,6,8,2,6]
l=[]
for i in range(len(arr)-1,-1,-1):
    if arr[i] not in l:
        l.append(arr[i])
    elif arr[i] in l:
        arr.pop(i)
        
print(arr)
