
x=input()
x=int(x)
a=0
b=0
c=1
count=99
if (x<100):
    print(x)

else:
    while(1):
        if (a == 10):
            b += 1
            a = 0

        if (b == 10):
            c += 1
            b = 0

        y = c * 100 + b * 10 + a

        if (x<y or c==10):
            break

        if ((a-b)==(b-c)):
            count+=1
        elif ((c-b)==(b-a)):
            count+=1

        a+=1
    print(count)

