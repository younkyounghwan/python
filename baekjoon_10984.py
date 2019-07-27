x = int(input())
for i in range(0,x):
    sum = 0
    cnt = 0
    y = int(input())
    for j in range(0,y):
        x, y = map(float,input().split())
        sum += x*y
        cnt += x
    print(int(cnt), sum/cnt)