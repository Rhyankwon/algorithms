'''
소프티어 5번 조립라인 해설
'''
import sys

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

# A쪽과 B쪽 각각 n번째까지 걸리는 최소 시간 저장하기.
result_A = []
result_B = []

# A, B는 A라인 B라인 최소 시간, wA는 A라인에서 B라인으로 옮길때 걸리는 시간. wB는 그 반대.
A = B = wA = wB = 0

for i in nums:
    # A(n)은 최솟값(A(n-1) + A라인 소요시간, B(n-1) + B에서 A라인으로 옮기는 시간 + A라인 소요시간)
    result_A.append(min(A + i[0], B + wB + i[0]))
    result_B.append(min(A + wA + i[1], B + i[1]))
    A, B = result_A[-1], result_B[-1]
    #마지막 라인에서는 wA, wB가 없다.
    if i != nums[-1]:
        wA, wB = i[2], i[3]
#n차까지 끝났을 때의 최솟값 반환.
print(min(A, B))