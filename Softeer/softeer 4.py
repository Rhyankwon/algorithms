'''
소프티어 4번 8단 변속기 문제 해설. 시간은 107ms, 메모리는 37mb가 소요됐다.
사실 이거랑 1번 문제는 난이도 별1개가 돼야하는게 아닌가 싶다. 너무 쉬워서 ...
조금의 파이썬 지식만 있어도 풀 수 있는 문제이긴한데 쉬운 만큼 조금 간단하게
코드를 짜보려고 노력하느라 시간이 꽤 소요된 것 같다. 그래도 마음에 드는 풀이.
'''

import sys
nums = list(map(int, input().split()))
result = []
for i in range(len(nums)-1):
    #뒷 값이 더 크면 True 입력, 모든 값이 True면 ascending. 모두 False면 descending 나머지 mixed.
    result.append((nums[i+1] - nums[i]) > 0)

if all(result):
    print('ascending')
elif any(result):
    print('mixed')
else :
    print('descending')