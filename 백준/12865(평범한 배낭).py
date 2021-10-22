# #풀이 1, 6808ms

# N, K = map(int, input().split())

# W = list()
# V = list()

# for i in range(N):
#     w, v = map(int, input().split())
#     W.append(w)
#     V.append(v)

# dp = [[0 for i in range(K+1)] for j in range(N)]

# for i in range(N):
#     for j in range(K+1):
#         if i == 0:
#             if W[i] <= j:
#                 dp[i][j] = V[i]
#         else:
#             if W[i] <= j:
#                 dp[i][j] = max(dp[i-1][j-W[i]]+V[i], dp[i-1][j])
#             else:
#                 dp[i][j] = dp[i-1][j]

# print(dp[N-1][K])


# #풀이 2, 1472ms

# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())

# dp = {0 : 0}

# for i in range(N):
#     tmp = {}
#     cur_w, cur_v = map(int, input().split())
#     for w, v in dp.items():
#         if w + cur_w <= K:
#             tmp[w+cur_w] = max(dp.get(w+cur_w, 0), v+cur_v)
#     dp.update(tmp)

# print(max(dp.values()))