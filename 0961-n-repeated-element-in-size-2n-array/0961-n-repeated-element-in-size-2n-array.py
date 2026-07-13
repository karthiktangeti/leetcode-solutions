class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        des = {}
        for i in nums:
            des[i] = des.get(i,0) + 1
        for key in des:
            if des[key] * 2 == len(nums):
                return key

        