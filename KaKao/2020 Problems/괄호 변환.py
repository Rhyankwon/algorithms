def split(p):
    dic1 = {'(' : 0, ')' : 0}
    for i in range(len(p)): #u,v로 나누기 전 u부분이 균형잡혔는지 확인
        dic1[p[i]] += 1
        if dic1['('] == dic1[')']:
            dic2 = {'(' : 0, ')' : 0}
            for j in range(i+1, len(p)): #v부분도 균형잡혔는지 확인
                dic2[p[j]] += 1
            if dic2['('] == dic2[')']:
                break
    return p[:i+1], p[i+1:]
        
def check_right(u): #올바른 괄호인지 확인
    stack = []
    for i in range(len(u)):
        if not stack:
            stack.append(u[i])
        elif stack[-1] != u[i] and stack[-1] == '(':
            stack = stack[:-1]
        else :
            stack.append(u[i])
    return True if not stack else False

def solution(p): #문제에서 제시된대로 구현
    empty_string = ''
    if p == '':
        return p
    u, v = split(p)
    if check_right(u):
        return u + solution(v)
    else :
        empty_string = '(' + solution(v) + ')'
        for i in range(1, len(u)-1):
            if u[i] == ')':
                empty_string += '('
            else :
                empty_string += ')'
        return empty_string