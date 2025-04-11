#Rotate the array to the left by k position.

arr = [2,4,6,8,10,12,14]

k = int(input('k = '))

for i in range(1,k+1):
    ele = arr[0]
    arr.remove(ele)
    arr.append(ele)

print(arr)
