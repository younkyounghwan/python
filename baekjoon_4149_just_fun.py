a = map(int,input())
while a>50:
    for i in range(2,a):
        if a == i+1:
            print(a)
            break
        if a%i == 0:
            break
    a+=1