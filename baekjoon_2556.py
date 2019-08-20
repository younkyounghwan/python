x = int(input())
if x == 1:
    print("*")
elif x== 2:
    print("**")
    print("**")
else:
    for i in range(0,x):
            for j in range(0,x):
                print("*",end="")
            print("")
