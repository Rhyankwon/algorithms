# 현대차 소프티어 20번 문제 해설 코드. GBC 문제!

import sys
import bisect

N, M = map(int,input().split())
limits = []
tests = []

for i in range(N):
    limits.append(list(map(int,input().split())))
    if i > 0:
        limits[-1][0] += limits[-2][0]

for i in range(M):
    tests.append(list(map(int,input().split())))
    if i > 0:
        tests[-1][0] += tests[-2][0]

p1 = p2 = 0
max_speed = 0
while p1 <= M - 1 and p2 <= N-1:
    speed = tests[p2][1] - limits[p1][1]
    max_speed = max(max_speed, speed)
    if limits[p1][0] < tests[p2][0] or p2 == M - 1:
        p1 += 1
    elif limits[p1][0] > tests[p2][0] or p1 == N - 1:
        p2 += 1
    else :
        p1 += 1
        p2 += 1

print(max_speed)