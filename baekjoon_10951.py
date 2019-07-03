l = []
while(True):
    try:
        a, b = map(int,input().split())
        l.append(a+b)
    except EOFError:
        break
for i in l:
    print(i)