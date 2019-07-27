a = int(input())
for i in range(0,a):
    b = int(input())
    player1 = 0
    player2 = 0
    for j in range(0,b):
        x, y = map(str,input().split())
        if x == "R":
            if y == "R":
                pass
            elif y == "S":
                player1 += 1
            else:
                player2 += 1
        elif x == "S":
            if y == "R":
                player2 += 1
            elif y == "S":
                pass
            else:
                player1 += 1
        else:
            if y == "R":
                player1 += 1
            elif y == "S":
                player2 += 1
    if player1 > player2:
        print("Player 1")
    elif player1 < player2:
        print("Player 2")
    else:
        print("TIE")