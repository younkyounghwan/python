x=1

while(1):

    a = 1
    b = 0
    c = 0
    d = 0
    if (x>18):
        a = 0
        b = 1
        c = 0
        d = 0
    if (x>117):
        a = 0
        b = 0
        c = 1
        d = 0
    if (x>1026):
        a = 0
        b = 0
        c = 0
        d = 1
    if (x>(1026+1001*1)):
        a = 0
        b = 0
        c = 0
        d = 2
    if (x>(1026+1001*2)):
        a = 0
        b = 0
        c = 0
        d = 3
    if (x>(1026+1001*3)):
        a = 0
        b = 0
        c = 0
        d = 4
    if (x>(1026+1001*4)):
        a = 0
        b = 0
        c = 0
        d = 5
    if (x>(1026+1001*5)):
        a = 0
        b = 0
        c = 0
        d = 6
    if (x>(1026+1001*6)):
        a = 0
        b = 0
        c = 0
        d = 7
    if (x>(1026+1001*7)):
        a = 0
        b = 0
        c = 0
        d = 8
    if (x>(1026+1001*8)):
        a = 0
        b = 0
        c = 0
        d = 9



    while(1):

        if (a==10):
            b+=1
            a=0

        if (b==10):
            c+=1
            b=0

        if (c==10):
            d+=1
            c=0

        y = d * 1000 + c * 100 + b * 10 + a

        if (x<=y):
            print(x)
            break

        if (x==(y + d + c + b + a) ):
            break

        a += 1

    if(x==10000):
        break

    x+=1