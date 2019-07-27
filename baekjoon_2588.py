x = int(input())
y = input()
mul = x*int(y)
for i in range(0,len(y)):
    print(x*int(y[len(y)-i-1]))
print(mul)