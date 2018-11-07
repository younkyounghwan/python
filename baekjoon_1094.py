x = int(input())
a=64
count = 0
while(1):
    if (x>=a):
        x-=a
        count+=1
    if (x<=0):
        break
    a//=2
print(count)
