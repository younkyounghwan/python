import sys
x = int(sys.stdin.readline())
for i in range(0,x):
    a, b = sys.stdin.readline().split()
    a = a.rstrip()
    b = b.rstrip()
    print(int(a)+int(b))