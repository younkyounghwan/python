x = input()
if x[0] == "A":
    if x[1] == '+':
        print(4.3)
    elif x[1] == '0':
        print(4.0)
    else:
        print(3.7)

elif x[0] == "B":
    if x[1] == '+':
        print(3.3)
    elif x[1] == '0':
        print(3.0)
    else:
        print(2.7)

elif x[0] == "C":
    if x[1] == '+':
        print(2.3)
    elif x[1] == '0':
        print(2.0)
    else:
        print(1.7)

elif x[0] == "D":
    if x[1] == '+':
        print(1.3)
    elif x[1] == '0':
        print(1.0)
    else:
        print(0.7)
else:
    print(0.0)