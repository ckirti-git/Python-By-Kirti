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


#------------------Using Sliding window-------------------------------

s = "abba"

start = 0
max_len = 0
max_sub = ""
char_index = {}

for end in range(len(s)):
    if s[end] in char_index and char_index[s[end]] >= start:
        start = char_index[s[end]] + 1  # Move start ahead of the repeated char

    char_index[s[end]] = end  # Update latest index of character

    window_len = end - start + 1
    if window_len > max_len:
        max_len = window_len
        max_sub = s[start:end+1]
    

print(max_len, '=', max_sub)
