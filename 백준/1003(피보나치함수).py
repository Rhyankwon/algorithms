#백준 1003번 피보나치 함수 파이썬 해설

import collections

class Solution:
    dp = collections.defaultdict(list)
    def fib(self, N):
        if self.dp[N]:
            return self.dp[N]
        if N == 0:
            return [1, 0]
        if N == 1:
            return [0, 1]
        else :
            self.dp[N] = [self.fib(N-1)[i] + self.fib(N-2)[i] for i in range(2)]
            return self.dp[N]
    def ans(self, N):
        print(*self.fib(N))

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

for i in nums:
    solution = Solution()
    solution.ans(i)

'''
풀이 2. 내꺼 맞추고 나서 다른사람들꺼 보고 참고한 코드
난..내코드도 좋지만 이 코드는 재귀가 아니라 반복을 활용했고 따로 값을 저장해두지 않아도 더 빠르게 값이 나온다.
'''
# class Solution:
#     def fib(self, N):
#         a, b = 0, 1
#         for i in range(N):
#             a, b = a+b, a
#         print(b, a)
# N = int(input())
# nums = []
# for i in range(N):
#     nums.append(int(input()))
# for i in nums:
#     solution = Solution()
#     solution.fib(i)