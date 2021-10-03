import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

dp = [sys.maxsize for i in range(k+1)]
dp[0] = 0

coins = sorted(list(set(coins)))

for c in coins:
    for j in range(1, k+1):
        if j >= c:
            dp[j] = min(dp[j-c] + 1, dp[j])

print([-1, dp[-1]][dp[-1]<sys.maxsize])