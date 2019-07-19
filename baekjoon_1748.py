import sys
x = int(sys.stdin.readline())
sum = 0

for i in range(1,x+1):
    sum += len(str(i))
print(sum)