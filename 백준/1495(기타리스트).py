N, S, M = map(int, input().split())

dif = list(map(int, input().split()))

dp = [[-1 for i in range(M+1)] for j in range(N+1)]

dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            if j - dif[i] >= 0:
                dp[i+1][j-dif[i]] = 1
            if j + dif[i] <= M:
                dp[i+1][j+dif[i]] = 1

ans = -1
for j in range(M+1):
    if dp[-1][j] == 1:
        ans = max(ans, j)

print(ans)