x = int(input())

cnt = 0
ck = 1
y = input().split()
for j in range(0,len(y)):
    y[j] = int(y[j])
for j in range(0, x):

    if j == 0:
        if y[0] == 1:
            cnt += ck
    elif y[j] == 1 :
        if y[j - 1] == 1:
            ck += 1
            cnt += ck
        else:
            cnt += 1
            ck = 1
print(cnt)