x = input()
x=int(x)

a=["  *  "," * * ","*****"]
b=[]


def cul(x):
    k = (x / 3)
    count = 0
    while (1):
        if (k == 1):
            break
        k /= 2
        count += 1
    return count