import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
com = [0 for i in range(n)]
dp = [[0 for i in range(n)]for j in range(3)]

s = int(input())

for i in range(n):
    if i >= (s-1):
        if com[i-1] == 0:
            com[i] = sum(nums[i-s+1:i+1])
        else :
            com[i] = com[i-1] + nums[i] - nums[i-s]

for i in range(3):
    for j in range(n):
        if i == 0 and j <= (n-2*s-1):
            dp[i][j] = max(dp[i][j-1], com[j])
        if i == 1 and 2*s-1 <= j <= (n-s-1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-s]+com[j])
        if i == 2 and 3*s-1 <= j:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-s]+com[j])

print(max(dp[2]))

# import sys #느린 버전

# input = sys.stdin.readline

# n = int(input())

# nums = list(map(int, input().split()))
# com = [0 for i in range(n)]
# dp = [[0 for i in range(n)]for j in range(3)]

# s = int(input())

# for i in range(n):
#     if i >= (s-1):
#         com[i] = sum(nums[i-s+1:i+1]) #이부분이 오래걸리게된다.

# for i in range(3):
#     for j in range(n):
#         if i == 0 and j <= (n-2*s-1):
#             dp[i][j] = max(dp[i][j-1], com[j])
#         if i == 1 and 2*s-1 <= j <= (n-s-1):
#             dp[i][j] = max(dp[i][j-1], dp[i-1][j-s]+com[j])
#         if i == 2 and 3*s-1 <= j:
#             dp[i][j] = max(dp[i][j-1], dp[i-1][j-s]+com[j])

# print(max(dp[2]))