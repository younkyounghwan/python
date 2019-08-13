x = int(input())
for i in range(x):
    a, b = map(str,input().split())
    for e in range(len(b)):
        for j in range(int(a)):
            print(b[e],end="")
    print("")