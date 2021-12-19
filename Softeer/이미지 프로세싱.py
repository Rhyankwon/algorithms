row, col = map(int, input().split())

grid = []

for i in range(row):
    grid.append(list(map(int, input().split())))

Q = int(input())

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def change(loc, color):
    global grid
    [i, j] = loc
    stack = [loc]
    tmp_color = grid[i][j]
    if tmp_color == color: #이미 같은 색인 경우 진행x. 이 부분에서 틀리는 사람 많을듯.
        return
    while stack:
        a, b = stack.pop()
        if 0 <= a < row and 0 <= b < col and tmp_color == grid[a][b]:
            grid[a][b] = c
            for i in range(4):
                stack.append([a+dir[i][0], b+dir[i][1]])

for que in range(Q):
    i, j, c = map(int, input().split())
    change([i-1, j-1], c)

for i in range(row):
    print(' '.join(map(str, grid[i])))