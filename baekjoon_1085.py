x = input().split()
for i in range(0,4):
    x[i] = int(x[i])
l = []
a = 1000
l.append(x[0])
l.append(x[1])
l.append(x[2]-x[0])
l.append(x[3]-x[1])
for i in range(0,4):
    if l[i] <= a:
        a = l[i]
print(a)