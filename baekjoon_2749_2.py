import sys
x = int(sys.stdin.readline())
a = 0
b = 1
c = a + b
if x == 1:
    print(a)
elif x == 2:
    print(b)
else:
    for _ in[0]*x:
        a = b
        b = c
        c = a + b
    print(a%1000000)