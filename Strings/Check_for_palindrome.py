#Check for palindrome.

s ="aabbcbbaa"
ans=[]
for i in reversed(s):
    ans.append(i)

fin = ''.join(ans)

if fin == s:
    print('Palindrome')
else:
    print('Not Palindrome')
