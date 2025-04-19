#Convert to title case.

s = "hello   world  lol"

l = s.split(' ')
l2=[]
for i in l:
    title = i[0].upper() + i[1:].lower()
    l2.append(title)

ans = ' '.join(l2)

print(ans)
