import sys
n = int(sys.stdin.readline())
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(n)%1000000)