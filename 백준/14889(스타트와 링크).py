import itertools
import sys

n = int(input())

arr_scores = []

for _ in range(n):
    arr_scores.append(list(map(int, input().split())))

ath = set([i for i in range(n)])
cand = sorted(list(itertools.combinations(ath, n//2)))
score = sys.maxsize
for i, c in enumerate(cand):
    c1, c2 = c, ath-set(c)
    score_1, score_2 = 0, 0
    for t1 in c1:
        for t2 in c1:
            if t1 == t2:
                pass
            else :
                score_1 += arr_scores[t1][t2]
    for t1 in c2:
        for t2 in c2:
            if t1 == t2:
                pass
            else :
                score_2 += arr_scores[t1][t2]
    score = min(score, abs(score_2-score_1))
    if score == 0 or i == len(cand)//2: #점수차 = 0 혹은 모든 경우를 다 체크한 경우 break.
        break

print(score)