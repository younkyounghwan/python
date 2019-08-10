def plus(a,b):
    result = a + space + b
    return result

n = int(input())

space = " "
messi_n2 = "Messi"
messi_n1 = "Messi Gimossi"
messi_n = "Messi Messi Gimossi"

while 1:
    if len(messi_n) >= n:
        break
    messi_n2 = messi_n1
    messi_n1 = messi_n
    messi_n = plus(messi_n2,messi_n1)

if messi_n[n-1] == " ":
    print("Messi Messi Gimossi")
else:
    print(messi_n[n-1])


