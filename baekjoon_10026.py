x = int(input())
l=[]
for i in range(0,x):
    y = input()
    l.append([])
    for j in range(0,x):
        l[i].append(y[j])
for i in range(0,x):
    print(l[i])