# import collections
# 현대차 소프티어 8, 9번 문제 해설 코드. 바이러스, 수퍼바이러스 문제!

K, P, N = map(int, input().split())
N *= 10

def pow(N):
    mod = 1000000007
    if N <= 1:
        return (P ** N) % mod
    if N % 2 == 0:
        return (pow(N//2) ** 2) % mod 
    elif N % 2 == 1:
        return ( P * pow(N//2) ** 2 ) % mod


print((K * pow(N)) % 1000000007)