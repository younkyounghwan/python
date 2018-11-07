n,x = input().split()
N=int(n)
X=int(x)
a = []
a = input().split()
A = []

for i in range(1,N+1):
    A.append(int(a[i-1]))

for i in range(1,N+1):
    if A[i-1] < X:
        print(A[i-1] ,end=" ")
