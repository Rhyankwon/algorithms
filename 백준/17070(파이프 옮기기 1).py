import sys
input = sys.stdin.readline

def dfs(x, y, shape): #dfs를 이용한 풀이
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return

    if shape == 0 or shape == 2:
        if y + 1 < n:
            if a[x][y+1] == 0:
                dfs(x, y+1, 0)
    if shape == 1 or shape == 2:
        if x + 1 < n:
            if a[x+1][y] == 0:
                dfs(x+1, y, 1)
    if shape == 0 or shape == 1 or shape == 2:
        if x + 1 < n and y + 1 < n:
            if a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, 1, 0)
print(ans)

# import sys
# input = sys.stdin.readline

# N = int(input())   #내가 처음 dfs로 풀었던 풀이. for문 때문인지 안됨
# grid = list(input().split() for i in range(N))

# info = {'right' : [0, 1], 'down' : [1, 0], \
#          'rightdown' : [1, 1]}
# candidates = {'right' : ['right', 'rightdown'], 'down' : ['down', 'rightdown'], \
#               'rightdown' : ['right', 'rightdown', 'down']}

# num = 0
# def dfs(path, index):
#     if index[0] == index[1] == N-1:
#         global num
#         num += 1
#     else :
#         for i in candidates[path[-1]]:
#             new_index = [index[0]+info[i][0], index[1]+info[i][1]]
#             if new_index[0] > N-1 or new_index[1] > N-1 or \
#                 grid[new_index[0]][new_index[1]] != '0' :
#                 continue
#             if i == 'rightdown' and '1' in [grid[new_index[0]-1][new_index[1]], \
#                 grid[new_index[0]][new_index[1]-1]]:
#                 continue
#             dfs(path+[i], new_index)

# dfs(['right'], [0, 1])
# print(num)

# import sys
# input = sys.stdin.readline   #dp풀이
# n = int(input()) 
# s = [list(map(int, input().split())) for i in range(n)]
# result = [[[0 for i in range(n)] for i in range(n)] for i in range(3)]
# result[0][0][1] = 1
# for i in range(2, n):
#     if s[0][i] == 0:
#         result[0][0][i] = result[0][0][i - 1]
# for i in range(1, n):
#     for j in range(2, n):
#         if s[i][j] == 0 and s[i - 1][j] == 0 and s[i][j - 1] == 0:
#             result[2][i][j] = result[0][i - 1][j - 1] + result[1][i - 1][j - 1] + result[2][i - 1][j - 1]
#         if s[i][j] == 0:
#             result[0][i][j] = result[0][i][j - 1] + result[2][i][j - 1]
#             result[1][i][j] = result[1][i - 1][j] + result[2][i - 1][j]
# print(result[0][n - 1][n - 1] + result[1][n - 1][n - 1] + result[2][n - 1][n - 1])
