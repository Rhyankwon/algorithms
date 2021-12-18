grid = []

for i in range(12):
    grid.append(list(input().strip()))

global visited

dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def dfs(loc):
    global grid
    [a, b] = loc
    color = grid[a][b]
    stack = [[a, b]]
    size = [] #크기가 4이상인지 확인하기 위해 잠시 저장해두기.
    while stack:
        [a, b] = stack.pop()
        if 0 <= a < 12 and 0 <= b < 6 and grid[a][b] == color and [a,b] not in visited:
            visited.append([a, b])
            size.append([a, b])
            for i in range(4):
                stack.append([a + dir[i][0], b + dir[i][1]])
    if len(size) >= 4:
        for [a, b] in size:
            grid[a][b] = '.'
        return 1
    else :
        return 0

ans = 0

while True:
    connected = []
    visited = []
    tmp = []
    for i in range(11, 0, -1):
        for j in range(6):
            if grid[i][j] != '.' and [i, j] not in visited:
                tmp.append(dfs([i, j]))
    if 1 in tmp:
        ans += 1
    else:
        break
    for i in range(11): #다시 맨 아래에서부터 문자로 채우기 위해 .있으면 윗쪽 값과 바꾸기. 
        for j in range(11, i, -1):
            for k in range(6):
                if grid[j][k] == '.':
                    grid[j-1][k], grid[j][k] = grid[j][k], grid[j-1][k]

print(ans)
