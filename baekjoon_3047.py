x = input().split()
for i in range(0,3):
    x[i] = int(x[i])
y = input()
l= []
if x[0] < x[1] and x[0] < x[2]:
    l.append(x[0])
    if x[1] < x[2]:
        l.append(x[1])
        l.append(x[2])
    else:
        l.append(x[2])
        l.append(x[1])

elif x[1] < x[0] and x[1] < x[2]:
    l.append(x[1])
    if x[0] < x[2]:
        l.append(x[0])
        l.append(x[2])
    else:
        l.append(x[2])
        l.append(x[0])

elif x[2] < x[1] and x[2] < x[0]:
    l.append(x[2])
    if x[1] < x[0]:
        l.append(x[1])
        l.append(x[0])
    else:
        l.append(x[0])
        l.append(x[1])

for i in range(0,3):
    if y[i] == 'A':
        print(l[0],end=" ")
    elif y[i] == 'B':
        print(l[1],end=" ")
    elif y[i] == 'C':
        print(l[2],end=" ")