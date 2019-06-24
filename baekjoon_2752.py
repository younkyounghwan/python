x = input().split()
for i in range(0,len(x)):
    x[i] = int(x[i])
if x[0] >= x[1]:
    if x[2] >= x[0]:
        max = x[2]
        if x[1] >= x[0]:
            a = x[1]
            b = x[0]
        else:
            a = x[0]
            b = x[1]
    else:
        max = x[0]
        if x[1] >= x[2]:
            a = x[1]
            b = x[2]
        else:
            a = x[2]
            b = x[1]
else:
    if x[2] >= x[1]:
        max = x[2]
        if x[1] >= x[0]:
            a = x[1]
            b = x[0]
        else:
            a = x[0]
            b = x[1]
    else:
        max = x[1]
        if x[2] >= x[0]:
            a = x[2]
            b = x[0]
        else:
            a = x[0]
            b = x[2]
print("%d %d %d" %(b, a, max))