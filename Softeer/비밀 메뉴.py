M, N, K = map(int, input().split())
secret = list(input().split())
custom = list(input().split())

if M > N:
    print('normal')
    exit(0)

if M == N:
    print(['secret', 'normal'][secret != custom])
    exit(0)

cur = []
for i in range(N - M + 1):
    cur = custom[i:i+M]
    if cur == secret:
        print('secret')
        exit(0)

print('normal')