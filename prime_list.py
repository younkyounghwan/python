x = int(input())
l = []
a = 1
for i in range(0,x-1):
    p = 1
    a += 1
    while(1):
        p += 1
        if a == p:
            l.append(a)
            break
        if a % p == 0:
            break