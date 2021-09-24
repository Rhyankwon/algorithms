N = int(input())

moo = ['m', 'o', 'o']
dp = [] #길이만 저장
dp.append(3)
for i in range(1, N+1):
    dp.append(0)
    dp[i] = dp[i-1] * 2 + i + 3
    if dp[i] >= N:
        break
n = N - 1
while True:    #앞, 가운데,뒤 3등분
    if i == 0:
        print(moo[n])
        break
    if n >= dp[i-1] + i + 3:
        n -= (dp[i-1] + i + 3)
        i -= 1
    elif n >= dp[i-1]:
        if n == dp[i-1]:
            print('m')
        else:
            print('o')
        break
    else:
        i -= 1