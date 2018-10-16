x = input()
y = input()
x = int(x)
y1 = int(y)
l=[]

sum = 0
for i in range(0,x):
    l.append(y[i])
for i in l:
    sum+=int(i)

print(sum)