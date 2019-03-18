sum = 0
max = 0
for i in range(0,10):
    x = input().split()
    for j in range(0,2):
        x[j] = int(x[j])
    sum -= x[0]
    sum += x[1]
    if sum >= max:
        max = sum
print(max)
    