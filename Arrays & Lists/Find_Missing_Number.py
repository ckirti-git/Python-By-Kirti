#Given numbers from 1 to n, one number is missing. Find it.

n = int(input('Enter the n= '))

a = sum(range(1,n+1),0)

arr = [1,2,3,4,5,7,8,9,10]

b = sum(arr,0)

num = a-b
print(num)
