l = []
k = []
for i in range(0,8):
    x = int(input())
    l.append(x)
d = sorted(l, key = int)
d = d[3:]
for i in range(0,5):
    p = l.index(d[i])
    k.append(str(p+1))
print(sum(d))
k.sort()
print(" ".join(k))