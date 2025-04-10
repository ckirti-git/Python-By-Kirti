#Find the second largest number in the array. ---------- Check again

arr = [1,2,6,8,10,23,14,11,70,88]

m = arr[0]

for i in arr:
    if m<i:
        m = i

arr.remove(m)

m = arr[0]
for i in arr:
    if m<i:
        m=i

print(m)
