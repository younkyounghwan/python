x = int(input())
l = []
for i in range(0,x):
    y = input().split()
    y[0] = int(y[0])
    y[1] = int(y[1])
    l.append(y)
for i in range(0,x):
    print("Case #" + str(int(i)+1) + ": " + str(l[i][0]) + " + " + str(l[i][1]) + " = " + str((l[i][0])+(l[i][1])))