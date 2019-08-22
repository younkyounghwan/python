import math
l = int(input())
r = int(input())
list = []
sum = 0
while 1:
    l = (l*r)//100
    if l <= 5:
        break
    list.append(l)
for i in range(len(list)):
    sum += list[i]*pow(2,i+1)
print(sum)