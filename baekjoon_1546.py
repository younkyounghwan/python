
x = input()
x = int(x)
s = input()
s = s.split()
for i in range(0,x):
    s[i] = float(s[i])
def big(x):
    a=0.0
    for i in range(0,x):
       if (s[i]>=a):
           a=s[i]
    return a
p = 100/big(x)
def aver(x):
    sum=0.0
    for i in range(0,x):
        sum+=s[i]
    return sum/x
print("%f"%(aver(x)*p))
