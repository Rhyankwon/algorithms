import sys
input = sys.stdin.readline
N = int(input())
arrs = []
for i in range(N):
    arrs.append(list(map(int, input().split())))

dp = [[0 for i in range(N)]for j in range(N)]

for i in range(1, N):
    for j in range(N-i):
        x = j+i
        dp[j][x] = sys.maxsize
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k]+dp[k+1][x]+arrs[j][0]*arrs[k][1]*arrs[x][1])

print(dp[0][N-1])