x = int(input())
l = []
for i in range(x):
    y = input()
    l.append(y)
for i in range(x):
    print("String #%d" %(i+1))
    for j in range(0,len(l[i])):
        if l[i][j] == "Z":
            print("A",end="")
        else:
            print(chr(ord(l[i][j])+1),end="")
    print("")
    print("")