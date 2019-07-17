x = int(input())
def star():
    print("*",end="")

def space():
    print(" ",end="")

if x == 1:
    print("*")
else:
    for i in range(0,x):
        if x%2 == 0:
            for j in range(0,x//2):
                star()
                space()
            print("")
            for j in range(0,x//2):
                space()
                star()
            print("")
        else:
            for j in range(0,x//2):
                star()
                space()
            print("*")
            for j in range(0,x//2):
                space()
                star()
            print("")