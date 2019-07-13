x = int(input())
a = input().split()
b = input().split()
for i in range(0,x):
    a[i] = int(a[i])
    b[i] = int(b[i])
d = b.copy()
a.sort()
d.sort()
sum = 0
for i in range(0,x):
    sum += a[i]*d[x-i-1]
print(sum)