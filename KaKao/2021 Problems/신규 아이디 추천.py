def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for w in new_id:
        if w.isalpha() or w.isdigit():
            answer += w
        elif w in '-_':
            answer += w
        elif w == '.':
            if not answer: 
                pass
            else :
                answer += ['', w][answer[-1] != w]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    if not answer:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]
    return answer