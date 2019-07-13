x = int(input())
for i in range(0,x):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r1 + r2 < (((x1-x2)**2)+((y1-y2)**2))**0.5:
        print(0)
    elif ((r1 -r2)**2)**0.5 > (((x1-x2)**2)+((y1-y2)**2))**0.5:
        print(0)
    elif r1 + r2 == (((x1-x2)**2)+((y1-y2)**2))**0.5:
        print(1)
    elif ((r1 -r2)**2)**0.5 == (((x1-x2)**2)+((y1-y2)**2))**0.5:
        print(1)
    else:
        print(2)