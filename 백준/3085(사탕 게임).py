import sys

input = sys.stdin.readline

N = int(input())
grid = [list(input().strip()) for i in range(N)]

def find(idx, length, dir, cnt):
    global visited
    global answer
    global grid
    [r, c] = idx
    tmp = grid[r][c]
    nr, nc = r + d[dir][0], c + d[dir][1]
    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid) \
       or visited[nr][nc]:
        answer = max(length, answer)
    else :
        if grid[nr][nc] == tmp:
            visited[nr][nc] = 1
            find([nr, nc], length+1, dir, cnt)
            visited[nr][nc] = 0
        else :
            if cnt == 1:
                answer = max(length, answer)
            else :
                for dr, dc in d:
                    fr, fc = nr+dr, nc+dc
                    if fr < 0 or fr >= len(grid) or fc < 0 or fc >= len(grid) \
                       or visited[fr][fc]:
                        answer = max(length, answer)
                    elif grid[fr][fc] == tmp:
                        grid[fr][fc], grid[nr][nc] = grid[nr][nc], grid[fr][fc]
                        visited[nr][nc] = 1
                        find([nr, nc], length+1, dir, cnt+1)
                        visited[nr][nc] = 0
                        grid[fr][fc], grid[nr][nc] = grid[nr][nc], grid[fr][fc]
                          
answer = -sys.maxsize
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for i in range(len(grid))]for j in range(len(grid))]

for i in range(len(grid)):
    for j in range(len(grid)):
        for k in range(4):
            visited[i][j] = 1
            find([i, j], 1, k, 0)
            visited[i][j] = 0
print(answer)