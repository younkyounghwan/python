x = int(input())
if x == 1:
    print("*")
elif x == 2:
    print(" *")
    print("**")
    print(" *")
else:
    for i in range(0,x):
        for j in range(0,x-i-1):
            print(" ",end="")
        for j in range(0,i+1):
            print("*",end="")
        print("")
    for i in range(x-1,0,-1):
        for j in range(0, x - i):
            print(" ", end="")
        for j in range(0, i):
            print("*", end="")
        print("")
