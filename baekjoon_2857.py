x = []
for i in range(0,5):
    a = input()
    x.append(a)
l = []
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        if x[i][j] == 'F':
            if len(x[i]) >= j+3:
                if x[i][j+1] == 'B' and x[i][j+2] == 'I':
                    l.append(i+1)
                    break
if not l:
    print("HE GOT AWAY!")
else:
    l = sorted(l)
    b = ''
    for i in range(0,len(l)):
        b = b + str(l[i])+' '
    print(b)