x = int(input())
l = []
for i in range(0,x):
    y = input()
    d = [1,2]
    d[0] = y[0]
    d[1] = y[2]
    d[0] = int(d[0])
    d[1] = int(d[1])
    l.append(d)
for i in range(0,x):
    print((l[i][0])+(l[i][1]))