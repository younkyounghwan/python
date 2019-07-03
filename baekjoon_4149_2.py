import sys
x = int(sys.stdin.readline())
p = 2
if x == 2:
    print(2)
elif x > 2:
    while(1):
        if p > x**(1/2):
            print(x)
            break
        elif x % p == 0:
            x = x//p
            print(p)
        elif x % p != 0:
            p += 2
            if p%3 == 0:
                p += 2
