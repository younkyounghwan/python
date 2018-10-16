s = input()
a = 0
b = 10
l = len(s)
print(s[a:b])
while(1):
    if (l>10):
        a+=10
        b+=10
        print(s[a:b])
        l-=10
    else:
        break
