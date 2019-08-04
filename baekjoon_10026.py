x = int(input())
l=[]
for i in range(0,x):
    y = input()
    l.append([])
    for j in range(0,len(y)):
        l[i].append(y[j])
for i in range(0,5):
    print(l[i])