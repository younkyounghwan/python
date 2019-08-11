n = int(input())

messi_n2 = "Messi "
messi_n1 = "Messi Gimossi "
messi_n = "Messi Gimossi Messi "

messi_2 = 6
messi_1 = 14
messi_0 = 20

messi_a = "A"
messi_b = "B"
messi_c = "BA"

cnt2 = 1
cnt1 = 1
cnt = 2

while 1:
    if messi_0 >= n:
        num = n - messi_1
        count = cnt - cnt1

        for i in range(count):
            if num > 14:

                if messi_c[cnt1+i] == "A":
                    num -= 6

                else:
                    num -= 14

            elif num > 6:
                if messi_c[cnt1+i] == "A":
                    num -= 6
                else:
                    break



            else:
                break

        break

    messi_2 = messi_1
    messi_1 = messi_0
    messi_0 = messi_1 + messi_2

    messi_a = messi_b
    messi_b = messi_c
    messi_c = messi_b + messi_a

    cnt2 = cnt1
    cnt1 = cnt
    cnt = cnt1 + cnt2

if n <= 14: #Messi Gimossi
    if messi_n[n-1] == " ":
        print(messi_n2 + messi_n1)
    else:
        print(messi_n1[n-1])

else: # Messi Gimossi
    if messi_n1[num-1] == " ":
        print("Messi Messi Gimossi")
    else:
        print(messi_n1[num-1])
