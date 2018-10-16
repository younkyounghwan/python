a = input()
count = 0
a=int(a)

if (a%3==1 and a<10):
    print(-1)

elif (a%3==0):
    while(1):
        if (a>=15):
            a-=15
            count+=3
        else:
            break
    while(1):
        if (a>=3):
            a-=3
            count+=1
        else:
            print(count)
            break

elif (a%3==1):
    a -= 10
    count += 2
    while (1):
        if (a >= 15):
            a -= 15
            count += 3
        else:
            break

    while (1):
        if (a >= 3):
            a -= 3
            count += 1
        else:
            print(count)
            break
            
elif (a%3==2):
    a-=5
    count+=1
    while(1):
        if (a>=15):
            a-=15
            count+=3
        else:
            break
    while (1):
        if (a >= 3):
            a -= 3
            count += 1
        else:
            print(count)
            break









