x = int(input())

count1 = 0
count2 = 0
if x == 0:
    print(0)
else:
    for i in range(1,x+1):
        while 1:
            if i/2 != i//2:
                break
            i = i//2
            count1 += 1
        while 1:
            if i/5 != i//5:
                break
            i = i//5
            count2 += 1
    if count1 >= count2:
        print(count2)
    else:
        print(count1)