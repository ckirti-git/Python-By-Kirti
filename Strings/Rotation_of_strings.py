#Check if two strings are rotations of each other.

str1 ="abc"
str2 ="acb"

s = str1+str1

if len(str1) == len(str2) and str2 in s:
    print('Valid Rotation')
else:
    print('Not Valid Rotation')
