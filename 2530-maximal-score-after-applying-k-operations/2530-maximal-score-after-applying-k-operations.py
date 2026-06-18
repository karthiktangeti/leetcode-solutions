import heapq
class Solution(object):
    def maxKelements(self, nums, k):
        nums = [-x for x in nums]
        heapq.heapify(nums)
        result = 0
        for i in range(k):
            j = - heapq.heappop(nums)
            result += j
            heapq.heappush(nums,-((j + 2) // 3))
        return result
