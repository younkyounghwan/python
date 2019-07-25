l = []
x, y =map(int,input().split()) #세로 가로
for i in range(0,x):
    for j in range(0,y):
        a = input()
        l.append(a)
if x == y:
    print(x**2)
elif x > y: # 세로 > 가로

    case = x - y +1
    sum = 0
    for i in range(0,case):
        for j in range(0,y):
            sum += l[j]

else: # 세로 < 가로
    print(0)