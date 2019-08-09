x = int(input())
y = x%14
if y == 0 or y == 6:
    print("Messi Messi Gimossi")
elif y == 1:
    print("M")
elif y == 2:
    print("e")
elif y == 3 or y == 4 or y == 11 or y == 12:
    print("s")
elif y == 5 or y == 8 or y == 13:
    print("i")
elif y == 7:
    print("G")
elif y == 9:
    print("m")
elif y == 10:
    print("o")