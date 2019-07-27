x, y, z = map(int,input().split())
y1 = ""
while 1:
    if y == 1:
        y1 += "1"
        break
    if y%2 == 1:
        y1 += "1"
        y = y//2
    else:
        y1 += "0"
        y = y//2
y = list(y1)
y.reverse() #reversed
trash = x%z
for i in range(1,len(y)):
    if y[i] == '0':
        trash = (trash**2)%z
    else:
        trash = (x*(trash**2))%z
print(trash)
