x = int(input())
y = int(input())
l = []
sum = 0
a = 2
i = 0
while(1):
    while(1):
        j = 1
        for i in range(2,a):
            if a%i == 0:
                a += 1
                j = i
                break
        if a%j != 0:
            break

    if a > y:
        break
    if a >= x:
        sum += a
        l.append(a)
if sum == 0:
    print(-1)
else:
    print(sum)
    print(l[0])
