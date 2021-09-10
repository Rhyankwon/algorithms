def solution(weights, head2head):
    info = []
    N = len(weights)
    for i in range(N):
        win = greater = 0
        num_plays = N - head2head[i].count('N') #전체 게임 횟수. L, W 수를 세면 됨.
        for j in range(N):
            if head2head[i][j] == 'W':
                win += 1 #win은 이긴 횟수
                if weights[j] > weights[i] :
                    greater += 1 #이겼을 때마다 몸무게 비교해서 상대가 더 무거우면 great +1
        if num_plays != 0:
            win /= num_plays
        info.append([win, greater, weights[i], i+1])
    info = sorted(info, key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    return [j[3] for j in info]
