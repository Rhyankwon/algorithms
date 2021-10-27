import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n, m = map(int, input().split())

words = []

for i in range(n):
    words.append(int(input()))

dp = [[-1 for i in range(m)]for j in range(n)]

def dfs(idx, tmp):
    if dp[idx][tmp] != -1:
        pass
    else :
        if idx == n-1:
            dp[idx][tmp] = 0
        else:
            if tmp + 1 + words[idx+1] < m :
                dp[idx][tmp] = min(dfs(idx+1, tmp+1+words[idx+1]), dfs(idx+1, words[idx+1]-1)+(m-tmp-1)*(m-tmp-1))
            else :
                dp[idx][tmp] = dfs(idx+1, words[idx+1]-1)+(m-tmp-1)*(m-tmp-1)
    return dp[idx][tmp]

print(dfs(0, words[0]-1))