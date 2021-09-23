import sys

N= int(input())
Eq = list(input())
result = -sys.maxsize

def cal(k, check):
    if k == 0:
        global result
        answer = [Eq[0]]
        for i in range(len(Eq)):
            if not Eq[i].isdigit():
                if check[i//2] == 1: #괄호로 묶인 경우를 먼저 모두 계산하면서 answer리스트에 연산 식 재구성.
                    answer = answer[:-1] + [str(eval(''.join(Eq[i-1:i+2])))]
                else:
                    answer = answer + Eq[i:i+2]

        while len(answer) > 1: #앞쪽부터 계산하기
            answer = [str(eval(answer[0]+answer[1]+answer[2]))] + answer[3:]
        if int(answer[0]) > result:
            result = int(answer[0])

    else :
        if not check or check[-1] == 0: #1은 괄호로 묶는 경우, 0은 아닌 경우. 직전에 괄호로 묶지 않으면(1이 아니면) 이번엔 괄호로 묶는 경우, 아닌 경우 둘 다 가능하다.
            cal(k-1, check+[1])
        cal(k-1, check+[0])

cal(N//2, [])
print(result)