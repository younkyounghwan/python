x = input()
x = int(x)
i = 0
l = []
while(1):
    if (x<(16**i)):
        break
    i+=1
i -= 1
y = i
while(1):
    a = x//16**i
    l.append(a)
    x-=a*(16**i)
    i-=1
    if (i<0):
        break
for k in range(0,y+1):
    for j in range(0,10):
        if (l[k]==j):
            print(l[k],end="")
    for j in range(10,16):
        if (l[k]==j):
            print(chr(l[k]+55),end="")