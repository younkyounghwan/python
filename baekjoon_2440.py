x = input()
x= int(x)
s="*"
k = s
l=[]
for i in range(0,x):
    l.append(k)
    k+=s
l.reverse()
for i in l:
    print(i)
