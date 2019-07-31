x = list(input())
for i in range(0,len(x)):
    x[i] = int(x[i])

diff = 0
a = 0
for i in range(0,len(x)-1):
    if i == 0:
        diff = x[i] - x[i+1]
    else:
        if diff != x[i] - x[i+1]:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            a += 1
            break
if a == 0:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
