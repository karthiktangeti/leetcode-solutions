class Solution(object):
    def lengthOfLIS(self, nums):
        def binary_search(target):
            l = 0
            r = len(res) - 1
            while l <= r:
                mid = (l + r) // 2
                if res[mid] == target:
                    return mid
                elif res[mid] > target:
                    r  = mid - 1
                else:
                    l = mid + 1
            return l


        res = []
        for i in nums:
            if not res or res[-1] < i:
                res.append(i)
            else:
                idx = binary_search(i)
                res[idx] = i
        return len(res)
            
        