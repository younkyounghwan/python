x = int(input())
def space(x):
    s = ""
    if x >= 2:
        for i in range(1,x):
            s = s + " "
    return s
def star(x):
    if x == 1:
        print("*")
    else:
        for i in range(0,x):
            print(space(x-i),end="")
            for j in range(0,(2*i+1)):
                print("*",end="")
            print("")
star(x)