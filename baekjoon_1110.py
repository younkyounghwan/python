x = input()
x = int(x)
count=1

def cul1(x): #1의 자리 수 반환
    a = x
    while(1):
        if (a<10):
            break
        a -= 10
    return a

def cul2(x):  # 10의 자리 수 반환
    a = x
    q=0
    while (1):
        if (a < 10):
            break
        a -= 10
        q += 1

    return q

def cut(x):

    if (x >= 10):
        a = x - 10
        return a
    else:
        return x

def plus(x):

    a = cul1(x)+cul2(x)
    return cut(a)


b = 10 * cul1(x) + plus(x)

while(1):

    if (x==b):
        print(count)
        break
    count+=1


    b = 10 * cul1(b) + plus(b)
