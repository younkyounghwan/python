t = int(input())
for i in range(0,t):
    time = 0
    n, k = map(int, input().split())
    y = input().split()
    nl = y.copy()
    for j in range(0,n):
        nl[j] = int(nl[j])
    kl = []
    for j in range(0,k):
        k1, k2 = map(int,input().split())
        kl.append([k1,k2])
    last = int(input())
    