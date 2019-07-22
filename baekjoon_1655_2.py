x = int(input())
y = int(input())
print(y)
a = 0
b = y
c = 0
for i in range(0,x-1):
    y = int(input())
    if i == 1:
        if y <= b:
            print(y)
            a = y
        else:
            print(b)
            c = y
    if i == 2:
        if y >= b:
            c = y
        elif y >= a:
            c = b
            b = y
        else:
            c = b
            b = a
            a = y
    
        