import sys

input = sys.stdin.readline

A, B = map(int, input().split())

def dfs(num, cnt):
    if num == B:
        print(cnt+1)
        exit(0)
    elif num > B:
        pass
    else :
        dfs(num*2, cnt+1)
        dfs(int(str(num)+'1'), cnt+1)

dfs(A, 0)
print(-1)