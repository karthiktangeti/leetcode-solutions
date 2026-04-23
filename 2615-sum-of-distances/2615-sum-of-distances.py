class Solution(object):
    def distance(self, nums):
        np = {}
        for i in range(len(nums)):
            if nums[i] not in np:
                np[nums[i]] = []
            np[nums[i]].append(i)
        res = [0] * len(nums)
        for indecies in np.values():
            n = len(indecies)
            total = sum(indecies)
            left_sum = 0
            for i in range(n):
                idx = indecies[i]
                right_sum = total - idx - left_sum
                left = idx * i - left_sum
                right = right_sum - idx * (n - i - 1)
                res[idx] = left + right
                left_sum += idx
        return res
            
        