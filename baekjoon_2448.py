x = input()
x = int(x)
s = ["  *  "," * * ","*****"]

def space(x):
    for i in range(0,x):
        print(" ",end="")

def new_line():
    print("\n")

def cul(x):
    k = (x / 3)
    count = 0
    while (1):
        if (k == 1):
            break
        k /= 2
        count += 1
    return count

def down(x,y):
    k = cul(x)-y
    return 3*2^k

def pict(n):
    print(s[n],end=" ")

def print_tree(x): 
    a = cul(x)
    for i in range(0,a+1): #3
        for j in range(0,3): #
            for m in range(0, 2^a): #4
                space(x - down(x, i))
                for r in range(0,2^a): #4
                    pict(j)

                    space(x - down(x, i))
            new_line()


print_tree(x)










