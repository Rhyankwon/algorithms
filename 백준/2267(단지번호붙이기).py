import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().strip())) for i in range(N)]

stack = []
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            stack.append([i, j])
            grid[i][j] = 0
            num = 0
            while stack:
                num += 1
                [a, b] = stack.pop()
                for dx, dy in dir:
                    x, y = a + dx, b + dy
                    if x >= 0 and x < N and y >= 0 and y < N and grid[x][y] == 1:
                        stack.append([x, y])
                        grid[x][y] = 0
            answer += [num]

print(len(answer))
for i in sorted(answer):
    print(i)