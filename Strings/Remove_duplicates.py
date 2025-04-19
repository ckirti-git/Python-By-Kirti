#Remove duplicates from string.

s = "abcabdcb"
l = []
l.extend(s)


for i in range(len(l)-1,-1,-1):
    sub_l = l[0:i]
    if l[i] in sub_l:
        l.pop(i)


s = ''.join(l)
print(s)
