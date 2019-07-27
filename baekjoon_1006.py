"""
step 1 입력단계
"""
T = int(input())
for i in range(0,T):
    l1 = []
    l2 = []
    count = 0
    minus = 0
    n, w = map(int,input().split())
    y = input().split()
    for j in range(0,n):
        l1.append(int(y[j]))

    y = input().split()
    for j in range(0, n):
        l2.append(int(y[j])) # 입력 완료




# step 2 필연적 독립수 분리
    for j in range(0,n):
        if j == 0:
            if l1[0] + l2[0] > w and l1[0] + l1[1] > w and l1[0] + l1[n-1] > w:
                l1[0] = w
                count += 1
            if l1[0] + l2[0] > w and l2[0] + l2[1] > w and l2[0] + l2[n-1] > w:
                l2[0] = w
                count += 1

        elif j == n-1:
            if l1[n-1] + l2[n-1] > w and l1[n-1] + l1[0] > w and l1[n-2] + l1[n-1] > w:
                l1[n-1] = w
                count += 1
            if l1[n-1] + l2[n-1] > w and l2[n-1] + l2[0] > w and l2[n-2] + l2[n-1] > w:
                l2[n-1] = w
                count += 1

        else:
            if l1[j] + l2[j] > w and l1[j] + l1[j+1] > w and l1[j] + l1[j-1] > w:
                l1[j] = w
                count += 1
            if l1[j] + l2[j] > w and l2[j] + l2[j+1] > w and l2[j] + l2[j-1] > w:
                l2[j] = w
                count += 1





#step 3 한면만 맞닿아 있는 수 찾기
    while 1:
        a = count

        for j in range(0,n):

            if j == 0: # 0일시

                if l1[0] != w:
                    #l1기준
                    if l1[1] == w and l1[n - 1] == w and l2[0] == w:
                        count += 1
                        l1[0] = w

                    elif l1[1] == w and l1[n-1] == w and l2[0] != w:
                        if l1[0] + l2[0] <= w:
                            count += 1
                            l1[0] = w
                            l2[0] = w
                        else:
                            count += 2
                            l1[0] = w
                            l2[0] = w

                    elif l1[1] == w and l1[n-1] != w and l2[0] == w:
                        if l1[0] + l1[n-1] <= w:
                            count += 1
                            l1[0] = w
                            l1[n - 1] = w
                        else:
                            count += 2
                            l1[0] = w
                            l1[n - 1] = w

                    elif l1[1] != w and l1[n-1] == w and l2[0] == w:
                        if l1[0] + l1[1] <= w:
                            count += 1
                            l1[0] = w
                            l1[1] = w
                        else:
                            count += 2
                            l1[0] = w
                            l1[1] = w

                if l2[0] != w:
                    #l2기준
                    if l2[1] == w and l2[n - 1] == w and l1[0] == w:
                        count += 1
                        l2[0] = w
                    elif l2[1] == w and l2[n - 1] == w and l1[0] != w:
                        if l2[0] + l1[0] <= w:
                            count += 1
                            l2[0] = w
                            l1[0] = w
                        else:
                            count += 2
                            l1[0] = w
                            l2[0] = w

                    elif l2[1] == w and l2[n - 1] != w and l1[0] == w:
                        if l2[0] + l2[n - 1] <= w:
                            count += 1
                            l2[0] = w
                            l2[n - 1] = w
                        else:
                            count += 2
                            l2[0] = w
                            l2[n - 1] = w

                    elif l2[1] != w and l2[n - 1] == w and l1[0] == w:
                        if l2[0] + l2[1] <= w:
                            count += 1
                            l2[0] = w
                            l2[1] = w
                        else:
                            count += 2
                            l2[0] = w
                            l2[1] = w

            if j == n-1: # n-1 일시
                if l1[n-1] != w:
                    #l1기준
                    if l1[0] == w and l1[n - 2] == w and l2[n - 1] == w:
                        count += 1
                        l1[n-1] = w

                    elif l1[0] == w and l1[n-2] == w and l2[n-1] != w:
                        if l1[n-1] + l2[n-1] <= w:
                            count += 1
                            l1[n-1] = w
                            l2[n-1] = w
                        else:
                            count += 2
                            l1[n-1] = w
                            l2[n-1] = w

                    elif l1[0] == w and l1[n-2] != w and l2[n-1] == w:
                        if l1[n-1] + l1[n-2] <= w:
                            count += 1
                            l1[n-1] = w
                            l1[n-2] = w
                        else:
                            count += 2
                            l1[n-1] = w
                            l1[n-2] = w

                    elif l1[0] != w and l1[n-2] == w and l2[n-1] == w:
                        if l1[n-1] + l1[0] <= w:
                            count += 1
                            l1[n-1] = w
                            l1[0] = w
                        else:
                            count += 2
                            l1[n-1] = w
                            l1[0] = w

                if l2[n - 1] != w:
                    #l2 기준
                    if l2[0] == w and l2[n - 2] == w and l1[n - 1] == w:
                        count += 1
                        l2[n-1] = w

                    elif l2[0] == w and l2[n-2] == w and l1[n-1] != w:
                        if l1[n-1] + l2[n-1] <= w:
                            count += 1
                            l1[n-1] = w
                            l2[n-1] = w
                        else:
                            count += 2
                            l1[n-1] = w
                            l2[n-1] = w

                    elif l2[0] == w and l2[n-2] != w and l1[n-1] == w:
                        if l2[n-1] + l2[n-2] <= w:
                            count += 1
                            l2[n-1] = w
                            l2[n-2] = w
                        else:
                            count += 2
                            l2[n-1] = w
                            l2[n-2] = w

                    elif l2[0] != w and l2[n-2] == w and l1[n-1] == w:
                        if l2[n-1] + l2[0] <= w:
                            count += 1
                            l2[n-1] = w
                            l2[0] = w
                        else:
                            count += 2
                            l2[n-1] = w
                            l2[0] = w

            else: #나머지 케이스
                if l1[j] != w:
                    #l1 기준
                    if l1[j + 1] == w and l1[j - 1] == w and l2[j] == w:
                        count += 1
                        l1[j] = w

                    elif l1[j+1] == w and l1[j - 1] == w and l2[j] != w:
                        if l1[j] + l2[j] <= w:
                            count += 1
                            l1[j] = w
                            l2[j] = w
                        else:
                            count += 2
                            l1[j] = w
                            l2[j] = w

                    elif l1[j+1] == w and l1[j - 1] != w and l2[j] == w:
                        if l1[j] + l1[j-1] <= w:
                            count += 1
                            l1[j] = w
                            l1[j-1] = w
                        else:
                            count += 2
                            l1[j] = w
                            l1[j-1] = w

                    elif l1[j+1] != w and l1[j - 1] == w and l2[j] == w:
                        if l1[j] + l1[j+1] <= w:
                            count += 1
                            l1[j] = w
                            l1[j+1] = w
                        else:
                            count += 2
                            l1[j] = w
                            l1[j+1] = w

                if l2[j] != w:

                    #l2 기준
                    if l2[j + 1] == w and l2[j - 1] == w and l1[j] == w:
                        count += 1
                        l2[j] = w

                    elif l2[j + 1] == w and l2[j - 1] == w and l1[j] != w:
                        if l2[j] + l1[j] <= w:
                            count += 1
                            l1[j] = w
                            l2[j] = w
                        else:
                            count += 2
                            l1[j] = w
                            l2[j] = w

                    elif l2[j + 1] == w and l2[j - 1] != w and l1[j] == w:
                        if l2[j] + l2[j - 1] <= w:
                            count += 1
                            l2[j] = w
                            l2[j - 1] = w
                        else:
                            count += 2
                            l2[j] = w
                            l2[j - 1] = w

                    elif l2[j + 1] != w and l2[j - 1] == w and l1[j] == w:
                        if l2[j] + l2[j + 1] <= w:
                            count += 1
                            l2[j] = w
                            l2[j + 1] = w
                        else:
                            count += 2
                            l2[j] = w
                            l2[j + 1] = w
        if a == count:
            break

#step 4 마무리 (이거 개빡셈)

