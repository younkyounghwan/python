l = []
while 1:
    x = input()
    if x == "END":
        break
    l.append(x[::-1])
for i in l:
    print(i)