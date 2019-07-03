for i in range(1000,10000):
    x = [] #16진수
    y = [] #12진수
    p = str(i) #10진수
    sum1 = 0
    sum2 = 0
    sum3 = 0
    a = hex(i)
    b = 3
    for j in range(2,len(a)): # 16진수 정렬
        if a[j].isdigit() == True:
            x.append(int(a[j]))
        else:
            x.append(ord(a[j])-87)

    while(1): #12진수 정렬
        if b < 0:
            break
        y.append(i//(12**b))
        i = i%(12**b)
        b -= 1
    for e in x:
        sum1 += e
    for f in y:
        sum2 += f
    for g in range(0,len(p)):
        sum3 += int(p[g])
    if sum1 == sum2 and sum1 == sum3:
        print(p)





