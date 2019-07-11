x = int(input())
sum = []
for i in range(0,x):
    count = []
    y = input()
    for j in range(0,26):
        count.append(0)
    for j in range(0,len(y)):
        if count[ord(y[j]) - 65] != 1:
            count[ord(y[j]) - 65] = 1
    sum.append(0)
    for j in range(0,26):
        if count[j] == 1:
            sum[i] += 65+j
for i in sum:
    print(2015-i)