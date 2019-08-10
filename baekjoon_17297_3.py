def plus(a,b):
    result = a + space + b
    return result

n = int(input())

space = " "
messi_n2 = "Messi"
messi_n1 = "Messi Gimossi"
messi_n = "Messi Messi Gimossi"

messi_a = 14
messi_b = 20
messi_c = 34
cnt = 0

while 1:
    if messi_c >= n:
        break
    messi_a = messi_b
    messi_b = messi_c
    messi_c = plus(messi_a,messi_b)
    
