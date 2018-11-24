sum = 1
for i in range(0,3):
    x = int(input())
    sum *= x
d = []
for i in range(0,10):
    d.append(0)
sum = str(sum)
for i in range(0,len(sum)):
    d[int(sum[i])] += 1
for i in d:
    print(i)