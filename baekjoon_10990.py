x= int(input())
if x == 1:
    print("*")
else:
    for i in range(0,x):
        for j in range(0,x-i-1):
            print(" ",end='')
        print("*",end='')
        if i != 0:
            for j in range(0,(i)*2-1):
                print(" ",end="")
            print("*")
        else:
            print("")