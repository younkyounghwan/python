x = int(input())
def star(x):
    for i in range(0,x):
        print("* ",end="")
    print("")
def space(x):
    for i in range(0,x):
        print(" *",end="")
    print("")
if x == 1:
    print("*")
elif x%2 == 1:
    for i in range(0,x//2):
        star(x)
        space(x)
    star(x)
else:
    for i in range(0,x//2):
        star(x)
        space(x)