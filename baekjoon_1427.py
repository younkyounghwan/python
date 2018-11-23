x = input()
l = []
for i in range(0,len(x)):
    l.append(x[i])
d = []

for i in range(0,len(x)):
    l[i] = int(l[i])
for i in range(0,len(x)):
    a = 0

    for j in range(0,len(l)):
        if l[j] >= a:
            a = l[j]
            b = j
    del l[b]
    d.append(a)
for i in range(0,len(d)):
    print(d[i],end="")
