N = int(input())

dp = [0 for i in range(N)]

for i in range(N):
    if i < 5:
        dp[i] = i+1
    else :
        tmp = 0
        for j in range(i-2):
            tmp = max(dp[j]*(i-(j+1)), tmp)
        dp[i] = tmp

print(dp[-1])