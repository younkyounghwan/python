x = int(input())
for i in range(0,x):
    c = 1
    a, b = map(int,input().split())
    if a%10 == 0:
        print(10)
    elif a%10 == 1:
        print(1)
    elif a%10 == 4:
        if b%2 == 1:
            print(4)
        else:
            print(6)
    elif a%10 == 5:
        print(5)
    elif a%10 == 6:
        print(6)
    elif a%10 == 9:
        if b%2 == 1:
            print(9)
        else:
            print(1)
    else:
        if (a%10)%2 == 1:
            if b%4 == 1:
                print(a%10)
            elif b%4 == 2:
                print(9)
            elif b%4 == 0:
                print(1)
            else:
                if a%10 == 3:
                    print(7)
                else:
                    print(3)
        else:
            if b%4 == 1:
                print(a%10)
            elif b%4 == 2:
                print(4)
            elif b%4 == 0:
                print(6)
            else:
                if a%10 == 2:
                    print(8)
                else:
                    print(2)