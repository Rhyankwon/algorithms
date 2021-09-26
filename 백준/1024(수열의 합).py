N, L = map(int, input().split())

while True:
    if L > 100:
        print('-1')
        break
    t = (L*L - L)//2
    if N-t >= 0 and (N-t)%L == 0:
        x = (N-t)//L
        for i in range(L):
            print(x+i, end = ' ')
        break
    L += 1