import sys
x = int(sys.stdin.readline())
sum = 0
if len(str(x)) == 9:
    print(788888898)

elif len(str(x)) == 8:
    sum += 68888897
    sum += (x-10000000)*8
    print(sum)
elif len(str(x)) == 7:
    sum += 5888896
    sum += (x-1000000)*7
    print(sum)

else:
    for i in range(1,x+1):
        sum += len(str(i))
    print(sum)

