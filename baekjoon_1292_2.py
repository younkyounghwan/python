l = []
x = int(input())
for i in range(1,x+1):
    a = i
    for j in range(1,i+1):
        l.append(a)
print(len(l))