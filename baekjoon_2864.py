x, y = map(str,input().split())
x = list(x)
y = list(y)
for i in range(0,len(x)):
    if x[i] == '5':
        x[i] = '6'
for i in range(0,len(y)):
    if y[i] == '5':
        y[i]= '6'
x = "".join(x)
y = "".join(y)
max = int(x) + int(y)
x = list(x)
y = list(y)
for i in range(0,len(x)):
    if x[i]  == '6':
        x[i] = '5'
for i in range(0,len(y)):
    if y[i] == '6':
        y[i] = '5'
x = "".join(x)
y = "".join(y)
min = int(x) + int(y)
print("%d %d" %(min,max))