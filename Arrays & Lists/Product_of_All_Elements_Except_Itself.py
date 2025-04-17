#Product of All Elements Except Itself -> For each element, print the product of all elements except itself. (no division)

arr = [5]

ans = []

for i in range(len(arr)):
    a = arr[i]
    idx = i

    arr[idx] = 1
    prod = 1
    for j in arr:
        prod = prod*j
    ans.append(prod)

    arr[idx]=a

print(ans)
