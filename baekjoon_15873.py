x = input()
sum = 0
for i in range(0,len(x)):
    sum += int(x[i])
    if int(x[i]) == 0:
        sum += (int(x[i-1])*9)
print(sum)