x = int(input())
l = []
for i in range(0,x):
    a = int(input())
    b = ''
    while(1):
        if a/2 > a//2:
            b = b+'1'
            d = a
            a = a//2
            if a == d:
                break
        else:
            b = b+'0'
            d = a
            a = a//2
            if a == d:
                break
    l.append(b)
for i in range(0,x):
    for j in range(0,len(l[i])):
        if l[i][j] == '1':
            print(j,end=" ")
    print('')