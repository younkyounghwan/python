x = int(input())
d = []
for i in range(0,x):
    y = input().split()
    y[0] = int(y[0])
    y[1] = int(y[1])
    d.append(y)
def combination(b,a):
    k = 1
    j = 1
    c = b
    for i in range(0,b):
        k *= a
        a -= 1
    for i in range(0,b):
        j *= c
        c -= 1
    return k//j
for i in range(0,x):
    print(combination(d[i][0],d[i][1]))