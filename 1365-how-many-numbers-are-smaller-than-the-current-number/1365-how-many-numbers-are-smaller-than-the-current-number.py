class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = nums[:]
        nums.sort()
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = i
        ans =[]
        for i in temp:
            ans.append(res[i])
        return ans


        