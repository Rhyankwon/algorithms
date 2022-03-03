import copy

global topni_arr
topni_arr = []

for _ in range(4):
    topni_arr.append(list(map(int, list(input()))))

N = int(input())

LEFT, RIGHT = 2, 6

def rot(t, d):
    tmp_row = []
    if d == 1:
        tmp_row = [topni_arr[t][-1]] + topni_arr[t][:-1]
    if d == -1:
        tmp_row = topni_arr[t][1:] + [topni_arr[t][0]]
    return tmp_row

def rot_system(t, d):
    global topni_arr
    tmp_arr = [[0 for i in range(len(topni_arr[0]))]for j in range(4)]
    tmp_arr[t] = rot(t, d)
    tmp_d = d
    for t_ in range(t+1, 4): #오른쪽으로 탐색
        if tmp_d != 0 and topni_arr[t_][RIGHT] != topni_arr[t_-1][LEFT]:
            tmp_d *= -1 #지난 톱니바퀴 방향과 반대로 움직인다.
            tmp_arr[t_] = rot(t_, tmp_d)
        else :
            tmp_arr[t_] = topni_arr[t_]
            tmp_d = 0 #만약 한번 안 움직이면 연쇄적으로 계속 안움직인다. tmp_d==0이면 단순 복사.
    tmp_d = d
    for t_ in range(t-1, -1, -1): #왼쪽으로 탐색
        if tmp_d != 0 and topni_arr[t_][LEFT] != topni_arr[t_+1][RIGHT]:
            tmp_d *= -1
            tmp_arr[t_] = rot(t_, tmp_d)
        else :
            tmp_arr[t_] = topni_arr[t_]
            tmp_d = 0
    topni_arr = copy.deepcopy(tmp_arr)

for _ in range(N):
    topni, dir = map(int, input().split())
    topni -= 1
    rot_system(topni, dir)

ans = 0
SCORE = 1
for i in range(4):
    if topni_arr[i][0] == 1:
        ans += SCORE
    SCORE *= 2 #점수 2배씩 증가

print(ans)