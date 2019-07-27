x = int(input()) # 2진수 변환기
s = ""
while 1:
    if x == 1:
        s += "1"
        break
    if x%2 == 1:
        s += "1"
        x = x//2
    else:
        s += "0"
        x = x//2
print("".join(reversed(s)))