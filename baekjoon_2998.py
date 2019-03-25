x = input()
y = list(x[::-1])
l = []
for i in range(0,len(y)//3):
    z = (x[3*i]*2 +x[3*i+1]*2 + x[3*i+2]*2)
    l.append(z)
l = l[::-1]
print(str(l))