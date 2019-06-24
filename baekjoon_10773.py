x = int(input())
l = []
for i in range(0,x):
    a = int(input())
    if a != 0:
        l.append(a)
    else:
        if l!=0:
            del l[-1]
print(sum(l))