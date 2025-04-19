#Replace all spaces with @.

s = " leading and trailing "
l = []
for i in s:
    if i == ' ':
        l.append('@')
    else:
        l.append(i)

ans = ''.join(l)
print(ans)
