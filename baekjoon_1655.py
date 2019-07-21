x = int(input())
l = []
for i in range(0,x):
    y = int(input())
    l.append(y)
    d = sorted(l,key = int)
    if i == 0:
        print(d[0])
    elif i == 1:
        if d[0] >= d[1]:
            print(d[1])
        else:
            print(d[0])
    else:
        if i%2 == 0:
            print(d[(i)//2])
        else:
            if d[(i+1)//2] >= d[(i+1)//2-1]:
                print(d[(i+1)//2-1])
            else:
                print(d[(i+1)//2])