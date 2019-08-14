n = int(input())
tile = []
for i in range(n):
    x = list(map(int,input().split()))
    tile.append(x)

for i in range(n-1):
    if min(tile[-1]) >= max(tile[-2]):
        break
    while 1:
        if min(tile[-1]) >= max(tile[i]):
            break

        if max(tile[i]) > min(tile[-1]):

            tile[-1][tile[-1].index(min(tile[-1]))] = max(tile[-2])
            tile[-2][tile[-2].index(max(tile[-2]))] = 0
answer = min(tile[-1])
print(answer)