#Length of Longest substring without repeating characters.

s = "abba"

max_len = 0
max_sub = ''

for k in range(len(s)):
    l = []
    for i in s[k:]:
        if i not in l:
            l.append(i)
        else:
            break
        
    if len(l) > max_len:
        max_len = len(l)
        max_sub = ''.join(l)


print(max_len,' = ',max_sub)
