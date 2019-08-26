T = int(input())
l = [2]
for _ in [0]*T:
    n = int(input())
    while 1:
        if a == n-1:
            break
        a = 3
        b = 2
        while 1:
            if b == a:
                l.append(a)
                break
            elif a%b == 0:
                break
            b += 1