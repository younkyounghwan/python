l = []
x = int(input())
for i in range(0,x):
    y = input()
    l.append(y)
print(" ".join(sorted(l,key = int)))