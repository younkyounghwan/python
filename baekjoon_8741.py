x = int(input())
sum = sum(range(2**x))
print(sum)
s = ""
while 1:
    if sum == 1:
        s += "1"
        break
    if sum%2 == 1:
        s += "1"
        sum = sum//2
    else:
        s += "0"
        sum = sum//2
print("".join(reversed(s)))