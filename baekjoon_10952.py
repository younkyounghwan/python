l = []
a = 0
while(1):
    x = input().split()
    x[0] = int(x[0])
    x[1] = int(x[1])
    if x[0]==0 and x[1]==0:
        break
    l.append(x)
    a += 1
for i in range(0,a):
    print(l[i][0]+l[i][1])