x = int(input())
for i in range(0,x):
    y = int(input())
    sum = 0
    z = input().split()
    for e in range(0,y):
        sum += int(z[e])
    print(sum)