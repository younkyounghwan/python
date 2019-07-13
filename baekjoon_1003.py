x = int(input())
for i in range(0,x):
    fi = [[1,0],[0,1]]
    y = int(input())
    if y == 0:
        print("%d %d" %(fi[0][0],fi[0][1]))
    elif y == 1:
        print("%d %d" %(fi[1][0],fi[1][1]))
    else:
        for j in range(0,y-1):
            fi.append([fi[j][0]+fi[j+1][0], fi[j][1]+fi[j+1][1]])
        print("%d %d" % (fi[-1][0], fi[-1][1]))