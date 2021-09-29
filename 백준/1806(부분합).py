import sys
input = sys.stdin.readline

N, S = map(int, input().split())

seq = list(map(int, input().split()))

left = 0
length = sys.maxsize
sum = 0
for i in range(len(seq)):
    sum += seq[i]
    while sum >= S:
        length = [length, i-left+1][length>(i-left+1)]
        sum -= seq[left] #조건 만족시 왼쪽 값 이동시켜서 가장 짧은 문자열 탐색
        left += 1

print([length, 0][length==sys.maxsize])