
# 이건 내 풀이

class Solution:
    def numIslands(self, grid):
        def check_island(i, j):
            if i >= 0 and i <= len(grid)-1 and j >= 0 and j <= len(grid[0])-1:
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    check_island(i-1, j)
                    check_island(i+1, j)
                    check_island(i, j-1)
                    check_island(i, j+1)
                    return 1
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += check_island(i, j)
        return count

# 파이썬 알고리즘 인터뷰 풀이
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def stack_push(index):
#             a, b = index[0], index[1]
#             if a < 0 or a > (len(grid)-1) or \
#                 b < 0 or b > (len(grid[0])-1):
#                 return
#             else :
#                 if grid[a][b] == '1':
#                     stack.append([a, b])
        
#         stack = []
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     stack.append([i, j])
#                     count += 1
#                     while stack:
#                         a, b = stack.pop()
#                         grid[a][b] = '0'
#                         stack_push([a-1, b])
#                         stack_push([a+1, b])
#                         stack_push([a, b+1])
#                         stack_push([a, b-1])
#         return count

solution = Solution()
nums = [["1","0","1","1","0","1","1"]]
print(solution.numIslands(nums))