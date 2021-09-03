import sys

def dfs(r, c, idx, total):
    global answer
    if answer > total + max_val * (3-idx):
        return
    if idx == 3:
        answer = max(answer, total)
        return
    for i in range(4):
        tmp_r = r + dr[i]
        tmp_c = c + dc[i]
        if tmp_r >= 0 and tmp_r < m and tmp_c >= 0 and tmp_c < n \
            and visited[tmp_r][tmp_c] == 0:
            if idx == 1:
                # ㅗ 모양에 대해 먼저 탐색
                visited[tmp_r][tmp_c] = 1
                dfs(r, c, idx+1, total+data[tmp_r][tmp_c])
                visited[tmp_r][tmp_c] = 0
            visited[tmp_r][tmp_c] = 1
            dfs(tmp_r, tmp_c, idx+1, total+data[tmp_r][tmp_c])
            visited[tmp_r][tmp_c] = 0

answer = 0
data = []
m, n = map(int, sys.stdin.readline().split())
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
for i in range(m):
    data.append(list(map(int,sys.stdin.readline().split())))
visited = [[0 for _ in range(n)] for _ in range(m)]
max_val = max(map(max, data)) #2차원 배열에서 가장 큰 값 찾기
for i in range(m):
    for j in range(n):
        visited[i][j] = 1
        dfs(i, j, 0, data[i][j])
        visited[i][j] = 0
print(answer)