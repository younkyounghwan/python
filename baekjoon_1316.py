x = int(input())
count = 0
for i in range(0,x):
    y = input()
    if len(y) == 1:
        count += 1
    elif y[len(y)-1] == y[len(y)-2]:
        count += 1
    else:
        for i in range(0,len(y)-1):
            if y[i] != y[i+1]:
                if y.count(y[i],i+1) > 0:
                    break
            if i == (len(y)-2):
                count += 1
print(count)