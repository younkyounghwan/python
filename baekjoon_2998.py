x = list(input())
y = x[::-1]
if len(y)%3 == 1:
    y.append(0)
    y.append(0)
if len(y)%3 == 2:
    y.append(0)
l = []
for i in range(0,len(y)//3):
    z = (int(y[3*i]) +int(y[3*i+1])*2 + int(y[3*i+2])*4)
    l.append(str(z))
print("".join(l[::-1]))