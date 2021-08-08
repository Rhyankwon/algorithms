class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x : x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            #병합하는 경우는 인덱스 위치 변경x if merged, no change on index
            else:
                i += 1
        return intervals

solution = Solution()
intervals = [[2,6], [10, 15], [15,18], [1,3], [5,6], [8,10]]
print(solution.merge(intervals))