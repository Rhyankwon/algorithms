import collections

class Solution:
    def cache(self, cacheSize, cities):
        queue = collections.deque(maxlen = cacheSize)
        count = 0
        for i in cities:
            i = i.lower()
            if i in queue:
                queue.remove(i)
                queue.append(i)
                count += 1
            else :
                # maxlen = cachesize -> if unnecessary
                # if len(queue) == 5:
                #     queue.popleft()
                queue.append(i)
                count += 5
        return count



cacheSize1 = 5
cacheSize2 = 3
cities = ["Jeju", "Pangyo", "Seoul", "Newyork", "LA", "Jeju", "Pangyo", "Seoul", "Newyork", "LA"]
solution = Solution()
print(solution.cache(cacheSize1, cities))
print(solution.cache(cacheSize2, cities))
