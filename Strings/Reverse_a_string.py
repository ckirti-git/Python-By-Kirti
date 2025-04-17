#Reverse a string.

s ="A man, a plan, a canal, Panama"
ans=[]
for i in reversed(s):
    ans.append(i)

fin = ''.join(ans)
print(fin)
