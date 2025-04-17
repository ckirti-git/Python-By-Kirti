##Majority Element -> Find the element that appears more than n/2 times (if any).

arr = [1, 2, 1, 1]

dic = {}
n = len(arr)
if n%2 == 0:
    times = n/2
else:
    times = n//2


for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic.update({i:1})


for j in dic:
    if dic[j] > times:
        ans = j
        break
    else:
        ans = 'no majority'

print(ans)
