import bisect
from itertools import combinations

def solution(info, query):
    cases = {}
    nums = []
    for idx, i in enumerate(info):
        i = i.split()
        sentence = i[:-1]
        for j in range(1, 5):
            for tmp in combinations(range(4), j):
                case = ''
                for k in range(4):
                    if k in tmp:
                        case += '-'
                    else :
                        case += sentence[k]
                if case not in cases:
                    cases[case] = []
                cases[case].append(int(i[-1]))
        if ''.join(sentence) not in cases:
            cases[''.join(sentence)] = []
        cases[''.join(sentence)].append(int(i[-1]))
    answer = []
    for value in cases.values():
        value.sort()
    for origin_q in query:
        origin_q = origin_q.split()
        tmp_q = ''.join([i for i in origin_q[:-1] if i != 'and'])
        if tmp_q not in cases:
            answer.append(0)
        else:
            cand = cases[tmp_q]
            b = bisect.bisect_left(cand, int(origin_q[-1]))
            answer.append(len(cand)-b)
    return answer