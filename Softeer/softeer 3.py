'''
소프티어 3번, 장애물 인식 프로그램 해설
스택을 써서 풀면 간단하게 풀리는 문제. 실행시간은 117ms, 메모리는 37MB가 소요됐다.
'''

import collections
import sys
M = int(input())
nums = [list(map(int, list(input()))) for _ in range(M)]
def check_hurdle(i, j):
    if i >= 0 and i <= M-1 and \
        j >= 0 and j <= M -1:
        if nums[i][j] == 1 and [i,j] not in stack:
            stack.append([i, j])
stack = list()
count = 0
result = []
for i in range(M):
    for j in range(M):
        if nums[i][j] == 1:
            stack.append([i, j])
            result.append(0)
            while stack:
                a, b = stack.pop()
                nums[a][b] = '#'
                result[-1] += 1
                check_hurdle(a-1, b)
                check_hurdle(a+1, b)
                check_hurdle(a, b-1)
                check_hurdle(a, b+1)
            count += 1
print(count)
result.sort()
for i in result:
    print(i)