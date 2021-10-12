import sys

input = sys.stdin.readline

N = int(input())
infos = []
for i in range(N):
    infos.append(list(map(int, input().split())))

Days = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
    if infos[i][0] + i <= N:
        Days[i] = max(Days[i+infos[i][0]] + infos[i][1], Days[i+1])
    else :
        Days[i] = Days[i+1]

print(Days[0])
