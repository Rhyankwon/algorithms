def solution(enter, leave):
    room = []
    answer = [0 for i in range(len(leave))]
    #Enter, Leave 각각 포인터 선언
    E = L = 0
    while True:
        while L < len(leave) and leave[L] in room:
            #leave의 맨 왼쪽부터, 퇴실시 이미 입실한 인원들에 +1 하고
            for r in room:
                if r != leave[L]:
                    answer[r-1] += 1
            #자기 자신에는 +(회의실에 남아있는 인원 수)
            room.remove(leave[L])
            answer[leave[L]-1] += len(room)
            #포인터 이동 후 퇴실 반복. 반드시 만나는 경우이므로 퇴실 가능시 무조건 퇴실시킨다.
            L += 1
        if E < len(enter):
            room.append(enter[E])
            E += 1
        if L == len(leave):
            #모두 나가면 break
            break
    return answer
