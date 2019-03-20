x = int(input())
l = []
for i in range(0,x):
    b = "x"
    a = input()
    for j in range(0, len(a)):
        if a[j] == "+":
            b = a.split("+")
            break
    l.append(b)
for i in range(0,x):
    if l[i] == "x":
        print("skipped")
    else:
        print(int(l[i][0]) + int(l[i][1]))