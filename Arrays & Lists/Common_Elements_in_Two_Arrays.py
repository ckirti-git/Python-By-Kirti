arr1 = [-1, 0, 1, 2]
arr2 = [-2, -1, 0, 3]

set1 = set(arr1)
set2 = set(arr2)

ans=[]

for i in set1:
    for j in set2:
        if i == j:
            ans.append(i)

print(ans)
