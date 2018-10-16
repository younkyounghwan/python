x,y=input().split()
x=int(x)
y=int(y)

def date(x,y):
    k = y
    if(x>2):
        k-=2
    if (x%2==1):
        for i in range(0,(x-1)//2):
            k+=61
        if (x>7):
            k+=1

    if (x%2==0):
        k+=31
        for i in range(1,(x//2)):
            k += 61

    return k

if(date(x,y)%7==1):
    print("MON")
if(date(x,y)%7==2):
    print("TUE")
if(date(x,y)%7==3):
    print("WED")
if(date(x,y)%7==4):
    print("THU")
if(date(x,y)%7==5):
    print("FRI")
if(date(x,y)%7==6):
    print("SAT")
if(date(x,y)%7==0):
    print("SUN")