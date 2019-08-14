A = []
B = []
answer = []

n, m = map(int,input().split())
for i in range(n):
    l = list(map(int,input().split()))
    A.append(l)

m, k = map(int,input().split())
for i in range(m):
    l = list(map(int,input().split()))
    B.append(l)

for i in range(n): # i = A의 세로 j = B의 가로 h = 접점

    answer.append([])
    for j in range(k):
        sum = 0
        for h in range(m):
            sum += (A[i][h] * B[h][j])
        answer[i].append(sum)
for i in answer:
    for j in i:
        print(j,end = " ")
    print('')
