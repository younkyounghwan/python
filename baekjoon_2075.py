n = int(input())
tile = []
for i in range(n):
    x = list(map(int,input().split()))
    tile.append(x)
answer = min(tile[-1])
list = []
for i in tile:
    for j in i:
        if j > answer:
            list.append(j)
for i in range(0,n-1):
    list.remove(max(list))
print(max(list))
