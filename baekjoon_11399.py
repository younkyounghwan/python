x = int(input())
y = input().split()
for i in range(0,len(y)):
    y[i] = int(y[i])
l = []
while(1):
    max = 0
    k = 0
    if not y:
        break
    for i in range(0,len(y)):
        if y[i] >= max:
            max = y[i]
            k = i
    l.append(max)
    del y[k]
l = l[::-1]
sum = 0
for i in range(0,x):
    for j in range(0,x-i):
        sum += l[j]
print(sum)
