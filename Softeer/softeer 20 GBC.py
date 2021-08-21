# 현대차 소프티어 20번 문제 해설 코드. GBC 문제!

import sys
import bisect

N, M = map(int,input().split())
limits = []
tests = []

for i in range(N):
    limits.append(list(map(int,input().split())))
    # 구간이 만약 50, 40, 10이면 50, 90, 100 이런 식으로 저장하기.
    if i > 0:
        limits[-1][0] += limits[-2][0]

for i in range(M):
    tests.append(list(map(int,input().split())))
    if i > 0:
        tests[-1][0] += tests[-2][0]

# 두 리스트 모두 정렬돼있으므로 투포인터 활용
p1 = p2 = 0
max_speed = 0
while p1 <= M - 1 and p2 <= N-1:
    # 두 리스트의 구간 중 하나라도 변경되면 답 업데이트
    speed = tests[p2][1] - limits[p1][1]
    max_speed = max(max_speed, speed)
    if limits[p1][0] < tests[p2][0] or p2 == M - 1:
        p1 += 1
    elif limits[p1][0] > tests[p2][0] or p1 == N - 1:
        p2 += 1
    # 두 포인터가 같은 곳에서 끝나는 경우, 가령 둘다 50m구간에서 끝날땐 포인터 둘 다 이동.
    else :
        p1 += 1
        p2 += 1

print(max_speed)