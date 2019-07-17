x = input()
l = list(x)
for i in range(0,len(x)):
    if ord(l[i]) > 96:
        l[i] = chr(ord(l[i]) - 32)
    else:
        l[i] = chr(ord(l[i]) + 32)
print("".join(l))