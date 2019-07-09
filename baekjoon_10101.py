l = []
sum = 0
for i in range(0,3):
    x = int(input())
    l.append(x)
    sum += x
if sum != 180:
    print("Error")
else:
    if l[0] == 60 and l[1] == 60:
        print("Equilateral")
    elif l[0] == l[1] or l[2] == l[1] or l[0] == l[2]:
        print("Isosceles")
    else:
        print("Scalene")