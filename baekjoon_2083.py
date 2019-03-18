l = []
while(1):
    x = input().split()
    if x[0] == "#":
        break
    l.append(x)

for i in range(0,len(l)):
    if int(l[i][1]) > 17 or int(l[i][2]) >= 80:
        print(l[i][0] + " Senior")
    else:
        print(l[i][0] + " Junior")