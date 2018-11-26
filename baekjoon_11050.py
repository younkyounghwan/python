x = input().split()
x[0] = int(x[0])
x[1] = int(x[1])
a = 1
b = 1
for i in range(0,x[1]):
    a *= x[0]
    x[0] -= 1
    b *= (i + 1)
print(a//b)
