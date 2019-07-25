import sys

N, W = map(int, sys.stdin.readline().split())
enemy = [int(data) for data in sys.stdin.readline().split()]
enemy2 = [int(data) for data in sys.stdin.readline().split()]
case = [[]] * 4
answer = []
case[0] = [[W+1] + enemy, [W+1] + enemy2]
case[1] = [[W+1] + enemy, enemy2[N-1:] + enemy2[:N-1] + [W+1]]
case[2] = [enemy[N-1:] + enemy[:N-1] + [W+1], [W+1] + enemy2]
case[3] = [enemy[N-1:] + enemy[:N-1] + [W+1], enemy2[N-1:] + enemy2[:N-1] + [W+1]]
for i in case:
    print(i)