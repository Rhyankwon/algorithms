import itertools
import collections

def solution(orders, course):
    answer = []
    sorted_orders = []
    for order in orders:
        sorted_orders.append(sorted(order))
    orders = sorted_orders
    for c in course:
        cand = set()
        tmp_answer = []
        for order in orders:
            if len(order) >= c:
                tmp_cand = set(itertools.combinations(order, c))
                tmp_answer.extend(list(tmp_cand & cand))
                cand = cand | tmp_cand
        count = collections.Counter(tmp_answer).most_common()
        if not count:
            continue
        answer.append(''.join(count[0][0]))
        for i in range(1, len(count)):
            if count[0][1] == count[i][1]:
                answer.append(''.join(count[i][0]))
    return sorted(answer)