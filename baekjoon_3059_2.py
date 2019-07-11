x = int(input()) # 입력 횟수
for j in range(0,x):
    y = input()
    alpha_count = []
    alpha = []
    a = 65
    for i in range(0,26):
        alpha_count.append(0)
        alpha.append(chr(a))
        a += 1
    for i in range(0,len(y)):
        if alpha_count[(ord(alpha[i]) - 65)] != 1:
            alpha_count[(ord(alpha[i]) - 65)] = 1
            alpha.remove()