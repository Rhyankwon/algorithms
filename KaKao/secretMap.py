class Solution:
    def secretMap(self, arr1, arr2, n):
        arr3 = []
        for i in range(n):
            arr3.append(bin(arr1[i]|arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' '))
        return arr3

solution = Solution()
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5
print(solution.secretMap(arr1, arr2, n))
