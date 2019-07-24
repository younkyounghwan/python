n, k = map(int,input().split())
l = []

for i in range(0,n):
    x = int(input())
    l.append(x)
d = sorted(l,key = int)
d = d.reverse()
