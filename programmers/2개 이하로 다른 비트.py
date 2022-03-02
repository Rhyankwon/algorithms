def solution(numbers):
    answer = []
    for n in numbers:
        tmp_n = bin(int(n))[2:][::-1]
        for i, s in enumerate(tmp_n):
            tmp_answer = tmp_n[:i]
            tmp = int(s) + 1
            flag = 0
            while tmp:
                if tmp == 2:
                    flag += 1
                    i += 1
                    tmp_answer += '0'
                else :
                    tmp_answer += '1'
                    break
                if flag == 2:
                    break
                if i < len(tmp_n):
                    tmp = 1 + int(tmp_n[i])
                else :
                    tmp = 1
            if flag in [0, 1]:
                answer.append(int((tmp_answer+tmp_n[i+1:])[::-1], 2))
                break
    return answer