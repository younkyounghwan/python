import sys
x = sys.stdin.readline()
x = int(x)
s = []
for i in range(0,x):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    s.append(a+b)
for i in range(0,x):
    print(s[i])