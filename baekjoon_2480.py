x = input().split()
sum = 0
for i in range(0,3):
    x[i] = int(x[i])
if x[0] == x[1] and x[1] == x[2]:
    print(x[0]*1000+10000)
else:
    if x[0] == x[1]:
        print(1000 + x[0] * 100)
    elif x[2] == x[1]:
        print(1000 + x[1] * 100)
    elif x[0] == x[2]:
        print(1000 + x[2] * 100)
    else:
        if x[0] >= x[2]:
            sum = x[0]
            if x[1] >= x[2]:
                sum = x[1]
            print(sum*100)
        else:
            sum = x[2]
            if x[1] >= x[2]:
                sum = x[1]
            print(sum*100)