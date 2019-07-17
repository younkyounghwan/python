x = input()
l = []
for i in range(0,26):
    l.append(0)
for i in range(0,len(x)):
    l[ord(x[i])-97] += 1
for i in range(0,26):
    l[i] = str(l[i])
print(" ".join(l))