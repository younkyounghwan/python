x = int(input())
l = []
k = 2
def is_prime(x):
    a= True
    b= False
    p=1
    if(x==1):
        return b
    while(1):
        p += 1

        if (x==p):
            return a
        if (x%p==0):
            return b
if x == 1:
    print(x)
else:
    while(1):
        if x == 1:
            for i in l:
                print(i)
            break
        if (x % k) == 0:
            l.append(k)
            x = x / k
        else:
            k += 1
            if is_prime(k) == True:
                if (x % k) == 0:
                    l.append(k)
                    x = x / k
