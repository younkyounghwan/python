x = int(input())
count = 0
for i in range(0,x):
    y = input()
    if len(y) == 1:
        count += 1
    elif len(y) == 2:
        count += 1
    else:
        for j in range(0,len(y)-1):
            if y[j] != y[j+1]:
                if y.count(y[j],j+1) > 0:
                    break
            if j == (len(y)-2):
                count += 1
                break
print(count)