def solution(n, build_frame):
    def impossible(answer):
        for b_f in answer:
            [x, y, a] = b_f
            if a == 0: #0은 기둥
                if y != 0 and [x-1, y, 1] not in answer and [x, y, 1] not in answer and\
                [x, y-1, 0] not in answer:
                    return 1
            if a == 1: #1은 보
                if [x, y-1, 0] not in answer and [x+1, y-1, 0] not in answer and\
                not ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    return 1
    answer = []
    for b_f in build_frame:
        if b_f[3] == 1: #추가
            answer.append(b_f[:3])
            if impossible(answer):
                answer.remove(b_f[:3])
        else: #제거
            answer.remove(b_f[:3])
            if impossible(answer):
                answer.append(b_f[:3])
    return sorted(answer)