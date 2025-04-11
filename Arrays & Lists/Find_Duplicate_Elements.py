#Identify and print duplicate values in the array.

arr = [1,2,4,5,1,6,8,9,2,9,3,4]

ans = []

for i in reversed(arr):
    a = i
    arr.remove(i)
    if a in arr:
        ans.append(a)

print(ans)
