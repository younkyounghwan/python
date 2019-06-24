l = []
while(1):
    count = 0
    max = 0
    x = input().split()
    for i in range(0,len(x)):
        x[i] = int(x[i])
        count += x[i]
    if count == 0:
        break
    if x[0] >= x[1]:
        if x[2] >= x[0]:
            max = x[2]
            a = x[1]
            b = x[0]
        else:
            max = x[0]
            a = x[1]
            b = x[2]
    else:
        if x[2] >= x[1]:
            max = x[2]
            a = x[1]
            b = x[0]
        else:
            max = x[1]
            a = x[0]
            b = x[2]
    if max**2 == a**2 + b**2:
        l.append('right')
    else:
        l.append('wrong')
for i in l:
    print(i)