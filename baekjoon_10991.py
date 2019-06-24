x = int(input())
y = x
count = 1
while(1):
    if x + 1 == count:
        break
    for i in range(0,y-1):
        print(" ",end="")
    for i in range(0,count):
        print("* ",end="")
    print("")
    count += 1
    y -= 1


