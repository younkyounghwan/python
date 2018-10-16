x = input()
x = int(x)
sum = 0
y = x
for i in range(0, x):
    y -= i
    sum += y
    y = x
print(sum)

