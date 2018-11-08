x = int(input())
n = input().split()
l=[]
d=[]
b=0
for i in range(0,x):
    for j in range(0,x):
        if i!=j:
            if n[i]==n[j]:
                b=1
for i in range(0,x):
    n[i] = int(n[i])
for j in range(0,x):
    a = 0
    for i in range(0,x):
        if n[i]>a:
            a = n[i]
            k = i
    d.append(k)
    n[k]=0


if b==1:
    for i in range(0,x):
        print(d[i], end=" ")
else:
    if x ==2:
        for i in range(x,0,-1):
            print(d[i-1],end=" ")
    else:
        for i in range(0,x-2):
            print(d[i], end=" ")
        for i in range(x,x-2,-1):
            print(d[i-1], end=" ")
