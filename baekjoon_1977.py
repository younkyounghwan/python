x = int(input())
y = int(input())
sum = 0
a = 1
l = []
while(1):
    if a**2 > y:
        break
    if a**2 >= x:
        sum += a**2
        l.append(a**2)
    a += 1
if sum != 0:
    print(sum)
    print(l[0])
else:
    print(-1)