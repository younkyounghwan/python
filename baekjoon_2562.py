l = []
a = 0
for i in range(0,9):
    x = int(input())
    l.append(x)
    for j in range(0,len(l)):
        if l[j] >= a:
            a = l[j]
            b = j
print(a)
print(b+1)