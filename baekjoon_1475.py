x = input()
d = []
for i in range(0,10):
    d.append(0)
for i in range(0,len(x)):
    d[int(x[i])] += 1
d[6] = (d[6] + d[9])
if d[6]%2 == 0:
    d[6] //= 2
else:
    d[6] //= 2
    d[6] += 1
del d[9]
print(max(d))