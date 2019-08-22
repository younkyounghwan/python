n = int(input())
l = []
for _ in [0]*n:
    x, y = map(int,input().split())
    l.append([y,x])
l.sort()
for i in range(n):
    print("%s %s" %(l[i][1],l[i][0]))
