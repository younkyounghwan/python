x = input()
x=int(x)
l=[]

def cul(x):
    k = (x / 3)
    count = 0
    while (1):
        if (k == 1):
            break
        k /= 2
        count += 1
    return count

def re(x):
    n = 0
    a = 0
    if (x >=12):
        for i in range(1,cul(x)):
            a += i
            n += a
        n += cul(x)
    return n

if (x == 3):
    n = 5
if (x == 6):
    n = 11
if (x >= 12):
    n = 5*2**cul(x)+re(x)

def space():
    l.clear()
    for i in range(0,n):
        l.append(" ")



for i in range(0,x//3):


    for p in range(0,x//3):
        for q in range(0,x//3):

            while(1):
                space()
                count = 0
                l[((n - 1) / 2)-3*count] = "*"
                l[((n - 1) / 2)+3*count] = "*"
                count+=1
                if (l[((n - 1) / 2)-3*count]==2):
                    break
                for j in l:
                    print(j,end="")
                print("")



        for q in range(0, x // 3):
            space()
            while(1):
                if (x==3):
                    l[((n - 1) / 2) + 1] = "*"
                    l[((n - 1) / 2) - 1] = "*"
                    break

                l[((n - 1) / 2) + 1] = "*"
                l[((n - 1) / 2) - 1] = "*"
                l[(((n - 1) / 2) - 3 * count)+1] = "*"
                l[(((n - 1) / 2) + 3 * count)-1] = "*"

                if (l[((n - 1) / 2)-3*count]==2):
                    break
                for j in l:
                    print(j,end="")
                print("")



        for q in range(0, x // 3):
            space()
            while(1):
                if (x == 3):
                    for r in range(0,5):
                        l[r]="*"
                    break

            for j in l:
                print(j,end="")
            print("")









