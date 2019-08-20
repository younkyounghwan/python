x = input()
d = len(x)
for i in range(0,len(x)):
    if x[i] == 'c':
        if len(x[i:]) >= 2:
            if x[i+1] == '=' or x[i+1] == '-':
                d -= 1

    elif x[i] == 'd':
        if len(x[i:]) >= 2:
            if x[i+1] == '-':
                d -= 1
        elif len(x[i:]) >= 3:
            if x[i+1] == 'z' and x[i+2] == '=':
                d -= 1

    elif x[i] == 'l':
        if len(x[i:]) >= 2:
            if x[i+1] == 'j':
                d -= 1

    elif x[i] == 'n':
        if len(x[i:]) >= 2:
            if x[i+1] == 'j':
                d -= 1

    elif x[i] == 's':
        if len(x[i:]) >= 2:
            if x[i+1] == '=':
                d -= 1

    elif x[i] == 'z':
        if len(x[i:]) >= 2:
            if x[i+1] == '=':
                d -= 1

print(d)
