x = int(input())
if x == 1:
    print("*")
elif x == 2:
    print(" * ")
    print("***")
else:
    for i in range(0,x):
        if i == 0:
            for j in range(0,x-1):
                print(" ",end="")
            print("*")
        elif i == x-1:
            for j in range(0,x*2-1):
                print("*",end="")
            print("")
        else:
            for j in range(0,x-i-1):
                print(" ",end="")
            print("*",end="")
            for j in range(0,i*2-1):
                print(" ",end="")
            print("*")
