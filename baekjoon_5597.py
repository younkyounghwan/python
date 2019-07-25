l = []
for i in range(0,30):
    l.append(str(i+1))
for i in range(0,28):
    x = input()
    l.remove(x)
for i in l:
    print(i)