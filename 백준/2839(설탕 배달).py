#백준 2839번 설탕 배달 문제

N = int(input())
# 5kg짜리 비닐봉지 쓰는게 이득이므로 일단 5kg에 가능한만큼 넣고
a, b = divmod(N, 5)
while True:
    # 남은걸 3kg 봉지에 모두 담을 수 있으면 끝
    if b % 3 == 0 :
        print(a + (b//3))
        break
    # 안되면 5kg짜리 비닐봉지에서 계속 빼기
    if a > 0:
        a -= 1
        b += 5
    else :
        print(-1)
        break