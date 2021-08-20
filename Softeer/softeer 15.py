
student, K = map(int,input().split())
grades = list(map(int,input().split()))

interval = []
for i in range(K):
    interval.append(list(map(int,input().split())))

result = []
for a, b in interval:
    result.append(sum(grades[a-1:b])/(b-a+1))

for i in result:
    print("{:.2f}".format(i))