T = int(input())

cases = []

for _ in range(T):
    cases += [int(input())]

c = max(cases) 
dp = [0 for i in range(c+1)]
dp[0] = 1
for i in range(1, 4):
    for j in range(len(dp)):
        if j >= i:
            dp[j] += dp[j-i]

for c in cases:
    print(dp[c])