x = int(input()) #역트리
def space(x):
    s = ""
    if x >= 1:
        for i in range(1,x):
            s = s + " "
    return s
def star(x):
    if x == 1:
        print("*")
    else:
        for i in range(0,x):
            print(space(i+1),end="")
            for j in range(0,(2*(x-i-1)+1)):
                print("*",end="")
            print("")
star(x)