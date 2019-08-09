n = int(input())
s = ""
for i in range(n):
    s += str(i+1)
n = str(n)
for i in range(int(s)):
    a = 0
    if s[i] == n[0]:
        for j in range(1,len(n)):
            if s[i+j] != n[j]:
                a = 1
                break
        if a == 0:
            k = i+1
            break
print(k)


