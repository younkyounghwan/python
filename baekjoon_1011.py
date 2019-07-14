x = int(input())
for i in range(0,x):
    a, b = map(int,input().split())
    d = b - a
    d1 = d**0.5
    k = (d1//1)*2+1
    if d == (d1//1)**2:
        k -= 2
    elif d <= (d1//1)**2 + (d1//1):
        k -= 1
    print("%d" %(k))