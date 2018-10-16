x,y=input().split()
x = x[::-1]
y = y[::-1]
x = int(x)
y = int(y)

if (x>=y):
    s=str(x)
else:
    s=str(y)

print(s)