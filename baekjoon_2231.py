x = int(input()) #분해합
a = 1 #생성자
b = 1 #연산자
while(1):
    sum = 0
    c = 1 #자리 수 확인장치
    while(1): #생성자의 자리 수 확인
        if a/b<10:
            break
        b *= 10
        c += 1
    b = 1
    d = a
    sum += d
    for i in range(0,c): #생성자로 분해합을 만들기
        e = (d//(10**(c-i-1)))
        sum += e
        d -= e*(10**(c-i-1))
    if x == sum: #일치 확인
        print(a)
        break
    a += 1
    if a >= x:
        print(0)
        break
