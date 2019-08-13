import math
x = int(input())
a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
a = math.ceil(a/a1)
b = math.ceil(b/b1)
if a>=b:
    print(x-a)
else:
    print(x-b)