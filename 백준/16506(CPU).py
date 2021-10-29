import sys

input = sys.stdin.readline

N = int(input())

orders = []

info = {'ADD' : 0, 'SUB' : 1, 'MOV' : 2, \
        'AND' : 3, 'OR' : 4, 'NOT' : 5, 'MULT' : 6, \
        'LSFTL' : 7, 'LSFTR' : 8, 'ASFTR' : 9,\
        'RL' : 10, 'RR' : 11}

for i in range(N):
    orders.append(list(input().split()))

ans = []

for op, rD, rA, rB in orders:
    tmp = ''
    tmp += str(bin(info[[op, op[:-1]][op[-1]=='C']])[2:]).zfill(4)
    tmp += ['00', '10'][op[-1] == 'C']
    tmp += str(bin(int(rD))[2:]).zfill(3)
    tmp += str(bin(int(rA))[2:]).zfill(3)
    tmp += str(bin(int(rB))[2:]).zfill([3, 4][op[-1] == 'C'])
    tmp += ['0', ''][op[-1] == 'C']
    ans.append(tmp)

for i in range(N):
    print(ans[i])