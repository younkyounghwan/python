l = []
p = []
x = int(input())
for i in range(0,x):
    y = input().split()
    for j in range(0,7):
        y[j] = int(y[j])
    l.append(y)
for i in l:
    sum = 0
    a = 100
    for j in range(0,7):
        if i[j]%2 == 0:
            sum += i[j]
            if i[j] <= a:
                a = i[j]
    p.append(str(sum) + " " + str(a))
for i in p:
    print(i)

