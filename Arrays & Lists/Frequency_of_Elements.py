#Print the frequency of each element in the list.

arr = [1,2,4,2,1,1,2,4,5,6,5,6,8,0,1,2,3,0]

dic = {}
l = []
l2 = []
for i in arr:
    key = i
    if key in dic:
        dic[key] +=1
    else:
        dic.update({key:1})
        l2.append(i)


for key in dic:
    l.append(dic[key])

print(l)
print(l2)
