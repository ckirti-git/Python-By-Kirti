#Remove duplicate characters using set.

ip = "hello world"

st = set()

s = ''

for i in ip:
    if i not in st:
        st.add(i)
        s+=i


print(s)
