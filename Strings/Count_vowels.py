#Count vowels and consonants.

s = 'abcabdcb'

v_cnt = 0
c_cnt = 0

for i in s:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        v_cnt+=1
    else:
        c_cnt+=1

print("Vowels = ",v_cnt)
print("Consonants = ",c_cnt)
