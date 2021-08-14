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
# 수학 문제에 가깝다. 규칙을 찾아서 그에 맞게 풀면 됨. 실행시간 106ms, 메모리 37.02로 통과
# 맨 처음에 자꾸 0점이 나와서 뭐지? 했는데 찾아보니 소프티어는 리트코드랑 문제풀이방식이 조금 다르다.
# 맨 처음에 import sys가 있어서 조금 이상하게 생각했는데 리스트를 인풋으로 읽어들이려면 당연히 필요한 부분이였다. 위에 내가 쓴대로 파이썬3에 실행하면 답이 바로 나오고, 소프티어에서 통과하려면

n = int(input())
mul = 0
for i in range(n):
    mul += 2 ** (i)
print((2 + mul) ** 2)

# 다음과 같이 써야 한다.
