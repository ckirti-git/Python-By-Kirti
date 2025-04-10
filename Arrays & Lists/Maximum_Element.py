#Find and print the maximum number from the list.

arr = [1,2,6,8,10,23,14,11,88]
m = arr[0]

for i in arr:
    if m<i:
        m = i

print(m)
