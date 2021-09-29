def solution(sizes):
    w = l = 0
    for i in sizes:
        [a, b] = i
        if a > b:
            a, b = b, a #작은 것들끼리, 큰 것들끼리 비교하기
        w = [w, a][a>w]
        l = [l, b][b>l]
    return w*l