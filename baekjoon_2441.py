x = input()
x= int(x)
s="*"
r=" "
l=[]
for i in range(0,x):
    l.append(s)
for i in range(0,x):
    if (i>=1):
        print("")
        l[i-1] = r
    for j in l:
        print(j,end="")