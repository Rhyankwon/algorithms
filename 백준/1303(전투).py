import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(input().strip()) for i in range(M)]

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def explore(r, c, color):
    stack = [[r,c]]
    grid[r][c] = 0
    num = 0
    while stack:
        x, y = stack.pop()
        num += 1
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if nx < M and nx >= 0 and ny < N and ny >= 0 and grid[nx][ny] == color \
               and [nx, ny] not in stack:
                grid[nx][ny] = 0
                stack.append([nx, ny])
    if color == 'B':
        B_power.append(num*num)
    elif color == 'W':
        W_power.append(num*num)

B_power = []
W_power = []

for i in range(M):
    for j in range(N):
        if grid[i][j] != 0:
            tmp = grid[i][j]
            explore(i, j, tmp)

print(sum(W_power), sum(B_power))