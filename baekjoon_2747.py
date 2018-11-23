x = int(input()) #항 입력
a = 0 # 앞 변수
b = 1 # 뒷 변수
for i in range(1,x): # 반복문
    c = a # 계산
    a = b
    b += c
print(b)