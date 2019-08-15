import math
n = int(input())
answer = []
for i in range(math.ceil(n/2)):
    l = list(map(int,input().split()))
    if i == 0:
        pass
    else:
        if l.index(max(l)) != l_index:
            del answer[0]
    l_index = l.index(max(l))
    answer.append(max(l))
for  i in range(n-math.ceil(n/2)):
    while 1:
        if len(answer) > n:
            answer.remove(min(answer))
        else:
            break

    l = list(map(int, input().split()))

    while 1:
        if min(answer) < max(l):
            answer.append(max(l))
            l[l.index(max(l))] = 0
        else:
            break

for i in range(n-1):
    answer.remove(max(answer))
print(max(answer))