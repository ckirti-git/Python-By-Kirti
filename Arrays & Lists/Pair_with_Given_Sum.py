#Check if any two numbers in the list add up to a target sum.

arr = [3, 5, 2, 8, 1, 9]
target = 10
ans = []
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        l = []
        if arr[i]+arr[j] == target:
            l.append(arr[i])
            l.append(arr[j])
            ans.append(l)

print(ans)
