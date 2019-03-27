x = int(input())
def space(x):
    s = ""
    if x >= 1:
        for i in range(1,x):
            s = s + " "
    return s
def block_star1(x):
    for i in range(0,x):
        for j in range(0,i + 1):
            print("*",end="")
        print(space(2*(x-i-1)+1),end="")
        for j in range(0, i + 1):
            print("*", end="")
        print("")

def block_star2(x):
    for i in range(0,x):
        for j in range(0,x-i-1):
            print("*",end="")
        print(space(2*(i+1)+1),end="")
        for j in range(0,x-i-1):
            print("*", end="")
        print("")
block_star1(x)
block_star2(x)