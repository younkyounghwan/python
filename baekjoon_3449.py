x = int(input())
l = []
for i in range(0,x):
    a = input()
    b = input()
    c = a + b
    l.append(c)
for i in range(0,x):
    count = 0
    for j in range(0,len(l[i])//2):
        if l[i][j] != l[i][j+len(l[i])//2]:
            count += 1
    l.append(count)
for i in range(x,x*2):
    print("Hamming distance is %s."%(l[i]))
