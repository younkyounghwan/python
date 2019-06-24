x = int(input())
p = 2
while(1):
    if x == p:
        print(x)
        break
    if x % p == 0:
        x = x//p
        print(p)
    if x % p != 0:
        p += 1