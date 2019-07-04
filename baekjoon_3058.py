l = []
p = []

x = int(input())
for i in range(0,x):
    y = map(int,input().split())
    l.append(y)
for i in y:
    sum = 0
    a = 100
    for j in range(0,len(str(i))):
        if str(i)[j]%2 == 0:
            sum += str(i)[j]
            if str(i)[j] <= a:
                a = str(i)[j]
        p.append(str(sum) + " " + str(a))
for i in p:
    print(p)

