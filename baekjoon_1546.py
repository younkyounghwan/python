s=[]
x = input()
x = int(x)
s[x]=input().split()
def big(x):
    a=0
    for i in range(0,x):
       if (s[i]>=a):
           a=s[i]
    return a
p = 100/big(x)
def aver(x):
    sum=0
    for i in range(0,x):
        sum+=s[i]
    return sum//x
print(aver(x)*p)