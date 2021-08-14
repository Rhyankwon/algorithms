import sys
class Solution:
    def autoMap(self, N):
        mul = 0
        for i in range(N):
            mul += 2 ** (i)
        return (2 + mul) ** 2

solution = Solution()
print(solution.autoMap(5))

# 현대차 소프티어 첫번째 문제. 지도 자동 구축.
# 수학 문제에 가깝다. 규칙을 찾아서 그에 맞게 풀면 됨. 실행시간 101ms, 메모리 37.28로 통과