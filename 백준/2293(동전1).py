import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

dp = [0 for i in range(k+1)]
dp[0] = 1

for c in coins:
    for m in range(1, k+1):
        if m >= c:
            dp[m] += dp[m-c]

print(dp[-1])