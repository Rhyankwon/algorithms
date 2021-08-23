#2019 카카오 블라인드 채용 2번 문제(실패율)

import collections

def solution(N, stages):
    count = collections.Counter(stages)
    players = sum(count.values())
    answer = []
    # pdb.set_trace()
    if not stages:
        return []
    for i in range(N):
        if not players:
            answer.append([0, i+1])
            continue
        answer.append([count[i+1]/players, i+1])
        players -= count[i+1]
    answer.sort(key = lambda x : (-x[0], x[1]))
    return [i[1] for i in answer]