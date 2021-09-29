import sys

N, K = map(int, sys.stdin.readline().strip().split())

k_list = list(map(int, sys.stdin.readline().strip().split()))

outlet = []
cnt = 0
for i in range(len(k_list)):
    if k_list[i] in outlet:
        k_list[i] = 0
    elif len(outlet) < N:
        outlet.append(k_list[i])
        k_list[i] = 0
    else :
        plug_out = []
        num = k_list[i]
        k_list[i] = 0
        for j in outlet:
            if j in k_list:
                plug_out.append([k_list.index(j), j])
            else:
                plug_out.append([100, j])   #뒷쪽에 다시 사용되는 경우 최우선순위로 사용. 
                break
        plug_out.sort()
        out = plug_out.pop()
        outlet.remove(out[1])
        outlet.append(num)
        cnt += 1
print(cnt)