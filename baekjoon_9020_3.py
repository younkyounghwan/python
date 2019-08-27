T = int(input())
l = []
a = 2
l.append(a)

while a<=9974:
    a += 1
    for i in range(2,a):
        if a%i == 0:
            break
    if i == a-1:
        l.append(a)

for _ in [0]*T:
    n = int(input())
    if n == 4:
        print("2 2")
    else:
        for i in range(n):
            if l[i] > n//2:
                break
            for j in range(len(l)-1,0,-1):
                if l[j] < n//2:
                    break
                if l[i] + l[j] == n:
                    s = str(l[i]) + " " + str(l[j])
        print(s)