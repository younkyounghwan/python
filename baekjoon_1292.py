x, y = map(int,input().split())
l = []
l.append(0)
for i in range(1,51):
    a = i
    for j in range(1,i+1):
        l.append(a)
l.append(0)
print(sum(l[x:y+1]))