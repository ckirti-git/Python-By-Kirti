#Are two strings anagrams?

str1 = 'triangle'
str2 = 'integral'

d1={}
d2={}

for i in str1:
    if i in d1:
        d1[i]+=1
    else:
        d1.update({i:1})

for j in str2:
    if j in d2:
        d2[j]+=1
    else:
        d2.update({j:1})


if len(str1) != len(str2):
    print('Not anagram')
else:
    if d1 == d2:
        print('Anagram')
    else:
        print("Not Anagram")
