n = int(input())

space = " "
messi_n2 = "Messi "
messi_n1 = "Messi Gimossi "
messi_n = "Messi Gimossi Messi "

messi_a = "A"
messi_b = "B"
messi_c = "BA"

while 1:
    if len(messi_n) >= n:
        break
    messi_n2 = messi_n1
    messi_n1 = messi_n
    messi_n = messi_n1 + messi_n2

    messi_a = messi_b
    messi_b = messi_c
    messi_c = messi_b + messi_a


if messi_n[n-1] == " ":
    print("Messi Messi Gimossi")
else:
    print(messi_n[n-1])
print(messi_c)