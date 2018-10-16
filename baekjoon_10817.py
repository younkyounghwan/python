x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)

if (x>=y and x>=z):
    if (y>=z):
        a=y
    else:
        a=z

elif (x < y and x >= z):
    a=x

elif (x >= y and x < z):
    a=x

elif (x < y and x < z):
    if (y>=z):
        a=z
    else:
        a=y
print(a)