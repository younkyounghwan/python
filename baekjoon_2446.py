x = int(input())
def space(x):
    s = ""
    if x >= 1:
        for i in range(1,x):
            s = s + " "
    return s
def star1(x): #트리
    if x == 1:
        print("")
    else:
        for i in range(1, x):
            print(space(x - i ), end="")
            for j in range(0, (2 * i + 1)):
                print("*", end="")
            print("")

def star2(x): #역트리
    if x == 1:
        print("*")
    else:
        for i in range(0,x):
            print(space(i+1),end="")
            for j in range(0,(2*(x-i-1)+1)):
                print("*",end="")
            print("")

star2(x)
star1(x)