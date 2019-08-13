e, s, m =map(int,input().split())
cnt = 1
e1 = 1
s1 = 1
m1 = 1
while 1:
    if e == e1 and s == s1 and m == m1:
        print(cnt)
        break
    cnt += 1
    e1 += 1
    s1 += 1
    m1 += 1
    if e1 == 16:
        e1 = 1
    if s1 == 29:
        s1 = 1
    if m1 == 20:
        m1 = 1
