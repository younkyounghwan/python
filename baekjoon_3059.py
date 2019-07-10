x = int(input())
q = [] #list include sum of alphabet

for i in range(0,x):
    a = 65
    l = []  # list included A to Z
    for i in range(0, 26):
        l.append(chr(a))
        a += 1  # how to make list l

    y = input()
    sum = 0
    for j in range(0,len(y)):
        l.remove(y[j])
    for j in range(0,len(l)):
        sum += ord(l[j])
    q.append(sum)
for i in q:
    print(i)