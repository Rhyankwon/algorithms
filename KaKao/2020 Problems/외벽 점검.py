# import itertools

# def solution(n, weak, dist):
#     answer = 10000
#     dist_cases = list(itertools.permutations(dist))
#     linear_weak = weak + [w+n for w in weak]
#     for j, w in enumerate(weak):
#         for cases in dist_cases:
#             start = w
#             for i, c in enumerate(cases):
#                 start += c
#                 if start < linear_weak[j+len(weak)-1]:
#                     start = [s for s in linear_weak[j+1:j+len(weak)] if s > start][0]
#                 else :
#                     answer = min(answer, i+1)
#                     break

#     return [-1, answer][answer != 10000]

def solution(n, weak, dist):
    repaired = [set()]
    count = 0
    linear_weak = weak + [w+n for w in weak]
    for d in dist[::-1]:
        new_repaired = set()
        count += 1
        for w in weak:
            avail = [s%n for s in linear_weak if w <= s <= w+d]
            for r in repaired:
                cand = set(r) | set(avail)
                if len(cand) == len(weak):
                    return count
                else :
                    new_repaired.add(tuple(cand))
        repaired = new_repaired
    return -1