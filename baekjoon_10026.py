x = int(input())
l=[[]]*5
for i in range(0,x):
    y = input()
    l.append([])
    for j in range(0,len(y)):

        l[i].append(y[j])

print(l)