import sys
x = sys.stdin.readline() #입력받을 짝수의 개수
x = int(x)
s=[]
a = 2
d=[]
while a<=9974: #d에 소수 리스트를 저장
    p=1
    while(1):
        p+=1
        if  (a==p):
            d.append(a)


        if (a%p==0):
            break
    a += 1
    if a%2 ==0 and a is nnot 
for i in range(0,x): #
    y = sys.stdin.readline()
    y = int(y)
    s.append(y)
for i in range(0, x):
    l=[]
    c=0
    while(1):
        if s[i]>9973:
            b = len(d)
            break
        if d[c] >= s[i]:
            b = len(d[:c])
            break
        c+=1
    e=0
    while(1):
        if d[e]>=s[i]//2:
            g = len(d[:e])
            break
        e+=1
    for j in range(0,g):
        for k in range(j,b):
            if s[i] < (d[j]+d[k]):
                k = b-1
            if s[i]==(d[j]+d[k]):
                l.append(d[j])
                l.append(d[k])
    if (len(l))%2==1:
        print("%d %d" %(l[len(l)-1], l[len(l)]))
    if (len(l))%2==0:
        print("%d %d" %(l[len(l)-2], l[len(l)-1]))