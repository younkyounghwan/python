x = int(input())
a = 0
b = 1
if x == 1:
    print(1)
else:
    for i in range(0,x-1):
        c = a + b
        a = b
        b = c
    print(c)