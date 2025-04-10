#Check if the array is sorted in ascending order or not.

arr = [10,23,14,11,70,88]


for i in range(1,len(arr)):
    if arr[i-1] <= arr[i]:
        ans = True
    else:
        ans = False
        break

if ans == True:
    print('sorted')
else:
    print('not sorted')
