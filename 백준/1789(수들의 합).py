N = int(input())
sum = 0
for i in range(N+1):
    sum += i
    if sum >= N:
        print([i, i-1][sum>N])
        break