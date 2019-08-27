n, m = map(int,input().split())
if n == 1:
    print(m-1)
elif m == 1:
    print(n-1)
else:
    print((n-1)+n*(m-1))