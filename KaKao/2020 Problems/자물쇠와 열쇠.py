def solution(key, lock):
    M, N = len(key), len(lock)

    global real_lock
    real_lock = [[1 for i in range(2*M + N -2)] for j in range(2*M + N -2)]
    
    def attach(i, j):
        for k in range(M):
            for l in range(M):
                real_lock[i+k][j+l] += key[k][l]

    def detach(i, j):
        for k in range(M):
            for l in range(M):
                real_lock[i+k][j+l] -= key[k][l]

    def check(i, j):
        for k in range(N):
            for l in range(N):
                if real_lock[i+k][j+l] != 1:
                    return False
        return True

    def rotate():
        r_key = list(zip(*key[::-1]))
        return r_key

    for i in range(N):
        for j in range(N):
            real_lock[M-1+i][M-1+j] = lock[i][j]
            

    for i in range(4):
        for j in range(M+N-1):
            for k in range(M+N-1):
                attach(j, k)
                if not check(M-1, M-1): #통과 못 하면
                    pass
                else :
                    return True
                detach(j, k)
        key = rotate()
    return False