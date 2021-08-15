import collections
import pdb

'''
혹시 누군가가 이 풀이를 가지고 수정한다음 소프티어에서 통과한다면 제게도 좀 알려주세요
처음풀이는 다소 중복되는 부분이 있어서 그 부분을 삭제했고 그 덕에 실행시간은 1639ms, 메모리는 40mb정도로 
처음 소프티어에서 제한한 수준까지 맞추긴 했습니다. 다만 답이 틀렸나봐요 아마도.. 득점은 여전히 빵점입니다.
정답이 아니니까 이걸 그대로 공부하진 마시고, 근데 아이디어는 제가 그렇게 틀리게 하진 않은 것 같아서.. 도움이 될지도 모르겠네요.
물론 나중에도 가끔 이 문제를 들여다보고 가능하다면 맞는 풀이로 만들어서 업데이트 할 생각입니다. 그때까지는
아래 솔루션은 정답이 아닙니다! 심지어 사이사이에 수정하는거라 처음에 제가 한것보다 더 틀려있을 수도 있어요 ㅋㅋ
'''

class Solution:
    def winterTest(self, M, N, nums):
        # 소프티어에 문제를 제출할때에는 아래의 두 라인을 추가해야함. 
        # M, N = map(int, input().split())
        # nums = [list(map(int, input().split())) for _ in range(M)]
        ice = collections.defaultdict(int)
        def ifout_(i, j):
            if i <= M-1 and i >= 0 and j >= 0 and j <= N - 1:
                # 외부 공기 옆에 얼음이 닿는 면이 있을 때마다 1 더함.
                if nums[i][j] == 1 :
                    ice[(i, j)] += 1
                # 옆쪽 아직 체크되지 않은 외부공기가 있는 경우 '#'처리(공기)
                elif nums[i][j] == 0:
                    nums[i][j] = '#'
                    outside.append([i, j])
        outside = [[0, 0]]
        # 총 얼음 갯수
        numice = sum(x.count(1) for x in nums)
        while outside:
            # 시작 시 한번 확인한 외부 공기는 전부 '#'표시.
            i, j = outside.pop()
            nums[i][j] = '#'
            ifout_(i-1, j)
            ifout_(i+1, j)
            ifout_(i, j-1)
            ifout_(i, j+1)
        count = 0
        melted_ice = 0
        while numice != melted_ice :
            count += 1
            for i in list(ice):
                # 외부 공기에 2번 이상 스친 경우 녹으니까 0으로 표지
                if ice[i] >= 2:
                    melted_ice += 1
                    nums[i[0]][i[1]] = 0
                    outside.append(i)
                    del ice[i]
            stack2 = outside[:]
            while outside:
                i, j = outside.pop()
                nums[i][j] = '#'
                ifout_(i-1, j)
                ifout_(i+1, j)
                ifout_(i, j-1)
                ifout_(i, j+1)
        if not numice :
            print(0)
        else :
            print(count)
            
solution = Solution()
nums = \
[[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]

solution.winterTest(8, 9, nums)
# print(solution.winterTest())