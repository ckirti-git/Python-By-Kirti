#Count word frequency in a string.

ip = "one two three one two"

l = ip.split(' ')
d={}

for i in l:
    if i in d:
        d[i]+=1
    else:
        d.update({i:1})

print(d)
