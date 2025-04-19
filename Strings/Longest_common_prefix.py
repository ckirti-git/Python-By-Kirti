#Longest common prefix.  

l = ["interview", "internet", "internal", "interval"]

base = l[0]
ans=''

for i in range(len(base)):
    match = True
    for word in l[1:]:
        if i>=len(word) or base[i]!=word[i]:
            match = False
            break

    if match:
        ans+=base[i]
    else:
        break

print(ans)
