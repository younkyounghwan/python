x = input()
x= int(x)
s="*"
r=" "
l=[]
for i in range(0,x):
    l.append(r)
for i in range(0,x):
    if (i>=1):
        print("")
    l[(x - 1) - i] = s
    for j in l:
        print(j,end="")