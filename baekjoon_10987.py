x = input()
l = ['a','e','i','o','u']
cnt = 0
for i in range(0,len(x)):
    for j in range(0,len(l)):
        if x[i] == l[j]:
            cnt += 1
            break
print(cnt)