#2019 카카오 블라인드 채용 1번 문제(오픈채팅방)

def solution(record):
    Id_list = {}
    answer = []
    _result = {0 : '님이 들어왔습니다.', 1 : '님이 나갔습니다.'}
    for i in record:
        user = i.split()
        sign, Id = user[0], user[1]
        if sign != 'Leave':
            name = user[2]
        if sign == 'Enter':
            Id_list[Id] = name
            answer.append([Id, 0])
        elif sign == 'Leave':
            answer.append([Id, 1])
        else :
            Id_list[Id] = name
    for i in range(len(answer)):
        answer[i] = Id_list[answer[i][0]]+_result[answer[i][1]]
    return answer