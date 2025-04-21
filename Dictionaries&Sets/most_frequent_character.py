#Find most frequent character.

ip = "aabbccddeeff"

d={}

for i in ip:
    if i in d:
        d[i]+=1
    else:
        d.update({i:1})
max=0
l=[]
for key in d:
    if max<=d[key]:
        max=d[key]
        l.append(key)

for j in l:
    print(j,':',d[j])
