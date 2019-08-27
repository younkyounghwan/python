sum1 = 0
cnt = 0
for i in range(5):
    x = list(map(int,input().split()))
    if sum(x) >= sum1:
        sum1 = sum(x)
        cnt = i + 1
print(cnt,sum1)