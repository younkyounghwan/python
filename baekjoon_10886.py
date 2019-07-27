cnt1 = 0
cnt2 = 0
x = int(input())
for i in range(0,x):
    y = int(input())
    if y == 1:
        cnt1 += 1
    else:
        cnt2 += 1
if cnt1 > cnt2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")