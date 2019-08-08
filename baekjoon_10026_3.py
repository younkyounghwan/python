import sys
sys.setrecursionlimit(100000)

N = int(input())

picture = [list(input()) for _ in range(N)] #갓댐.....

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(pic, y, x):
    visited[y][x] = True

    for next in range(4):
        nextX, nextY = x + dx[next], y + dy[next]
        if (0 <= nextX < N) and (0 <= nextY < N) and pic[y][x] == pic[nextY][nextX] and visited[nextY][nextX] is False:
            dfs(pic, nextY, nextX)

def abnormal(pic):
    for line in pic:
        for char in range(len(line)):
            if line[char] == 'G':
                line[char] = 'R'


section = [0, 0]

for cnt in range(2):
    visited = [[False for _ in range(N)] for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if visited[row][col] is False:
                dfs(picture, row, col)
                section[cnt] += 1

    abnormal(picture)

print(section[0], section[1])