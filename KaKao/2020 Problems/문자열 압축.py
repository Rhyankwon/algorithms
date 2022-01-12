import sys

def check(i, string):
    new_s = ''
    tmp = 0
    while tmp <= len(string):
        cnt = 1
        sub_string = string[tmp:tmp+i]
        for j in range(1, len(string)):
            if len(string[tmp+j*i:tmp+(j+1)*i]) >= i and string[tmp+j*i:tmp+(j+1)*i] == sub_string:
                cnt+=1
            else:
                break
        if cnt == 1:
            new_s += sub_string
        else :
            new_s += str(cnt) + sub_string
        tmp += j*i
    new_s += string[tmp:]
    return len(new_s)

def solution(s):
    global answer
    N = len(s)//2
    answer = sys.maxsize
    for i in range(1, N+1):
        answer = min(check(i, s), answer)
    if answer != sys.maxsize:
        return answer 
    else:
        return 1