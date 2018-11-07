x = input()
x = int(x)
s=[]
def aver(x):

    return sum(x)/len(x)
def aver1(x):

    count = 0
    for i in range(0,len(x)):
        if x[i]>aver(x):

            count +=1
    return (count/len(x))*100
for i in range(0,x):
    y=input()
    y=y.split()
    y[0] = int(y[0])
    for j in range(0,y[0]):
        y[j+1]= float(y[j+1])
    del y[0]
    s.append(y)

for i in range(0,x):
    print("%.3f"%aver1(s[i]),end="%")
    print("")

