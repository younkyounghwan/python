a, b = map(int,input().split())
c, d = map(int,input().split())
sum = 0
for i in range(0,4):
    if (a/c + b/d) >= sum:
        sum = (a/c + b/d)
        j = i
    k = a
    a = c
    c = d
    d = b
    b = k
print(j)