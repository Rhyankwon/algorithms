import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for i in range(N)] for j in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        jump = board[i][j]
        if jump == 0:
            break
        if i + jump < N:
            dp[i+jump][j] += dp[i][j]
        if j + jump < N:
            dp[i][j+jump] += dp[i][j]

print(dp[N-1][N-1])