import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

waste = []
for i in range(K):
    waste.append(list(map(int, input().split())))

grid = [[0 for i in range(M)] for j in range(N)]

for r, c in waste:
    grid[r-1][c-1] = 1

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

answer = 0

def explore(r, c, color):
    global answer
    stack = [[r,c]]
    grid[r][c] = 0
    num = 0
    while stack:
        x, y = stack.pop()
        num += 1
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if nx < N and nx >= 0 and ny < M and ny >= 0 and grid[nx][ny] == color \
               and [nx, ny] not in stack:
                grid[nx][ny] = 0
                stack.append([nx, ny])
    answer = [answer, num][num>answer]

for i in range(N):
    for j in range(M):
        if grid[i][j] != 0:
            tmp = grid[i][j]
            explore(i, j, tmp)

print(answer)